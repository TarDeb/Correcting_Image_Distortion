import cv2
import numpy as np
import os
import glob

input_folder_path = "T_images"  # Replace with your input folder path
output_folder_path = "T_imagesCorrectNew"  # Replace with your output folder path

# Ensure the output folder exists, create it if not
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)


def correct_distortion(img, k1, k2, p1, p2, k3, rotation_angle):
    h, w = img.shape[:2]
    camera_matrix = np.array([[766.14, 0, w / 2.0], [0, 766.14, h / 2.0], [0, 0, 1]])

    # Updated distortion coefficients for cv2.undistort function
    dist_coeffs = np.array([k1, k2, p1, p2, k3], dtype=np.float64)

    img_undistorted = cv2.undistort(img, camera_matrix, dist_coeffs)

    M = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), rotation_angle, 1)
    img_rotated = cv2.warpAffine(img_undistorted, M, (w, h))

    step_size = 60
    for i in range(0, w, step_size):
        cv2.line(img_rotated, (i, 0), (i, h), (0, 255, 0), 1)
    for i in range(0, h, step_size):
        cv2.line(img_rotated, (0, i), (w, i), (0, 255, 0), 1)

    return img_rotated


def process_images(input_folder, output_folder):
    image_files = glob.glob(os.path.join(input_folder, "*.JPG"))
    image_files += glob.glob(os.path.join(input_folder, "*.jpg"))  # To include .jpg files

    if not image_files:
        print(f"No image files found in {input_folder}")
        return

    k1, k2, p1, p2, k3, rotation_angle = -0.35245767, 0.13652994, 0, 0, 0.1339468, -2  # Update with your coefficients

    for file in image_files:
        img = cv2.imread(file)
        if img is None:
            print(f"Failed to read {file}")
            continue

        img_corrected = correct_distortion(img, k1, k2, p1, p2, k3, rotation_angle)

        filename = os.path.basename(file)
        output_file_path = os.path.join(output_folder, "corrected_" + filename)

        if cv2.imwrite(output_file_path, img_corrected):
            print(f"Successfully wrote {output_file_path}")
        else:
            print(f"Failed to write {output_file_path}")


if __name__ == "__main__":
    process_images(input_folder_path, output_folder_path)
