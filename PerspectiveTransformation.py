import cv2
import numpy as np

points = []  # List to store the coordinates of the points selected by the user

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 4, (0, 255, 255), -1)  # Draw a circle at the clicked position
        points.append((x, y))  # Append the coordinates to the points list
        print(x, y)  # Print the coordinates to the console
        cv2.imshow('Image', img)
        if len(points) == 4:  # If four points have been selected, perform the perspective transformation
            warp_perspective()

def warp_perspective():
    width, height = 400, 600  # Dimensions of the output image
    pts1 = np.float32(points)  # Coordinates of the points selected by the user
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Coordinates of the points in the output image
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # Compute the perspective transformation matrix
    result = cv2.warpPerspective(img, matrix, (width, height))  # Apply the matrix to warp the image
    cv2.imshow('Original Image', img)  # Display the original image
    cv2.imshow('Warped Perspective Image', result)  # Display the warped image

if __name__ == "__main__":
    img = cv2.imread("../corrected.JPG")  # Load the image
    cv2.imshow('Image', img)  # Display the image
    cv2.setMouseCallback('Image', click_event)  # Set the mouse callback to the click_event function
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the windows
