# Correcting_Image_Distortion
This repository contains a Python script for image processing using OpenCV
 The script reads images from a specified folder, corrects distortion using given camera matrix and distortion coefficients, rotates the images by a specified angle, draws a grid on them, and then saves them to a specified output folder.

## Introduction

In digital image processing, correcting image distortion is crucial for accurate representation. This script focuses on undoing the distortion in images and performing additional processing like rotation and drawing grid lines, which can be useful in various applications like computer vision, robotics, and photography.

## Usage

- Ensure you have Python installed along with required libraries: OpenCV and NumPy.
- Replace the input and output folder paths with your folder paths.
- Run the script: `python image_processing.py`
# Original Photo
![image](https://github.com/TarDeb/Correcting_Image_Distortion/assets/105755292/94b17e05-2088-4dd1-ad95-0356cebc033f)

# Corrected Image
![image](https://github.com/TarDeb/Correcting_Image_Distortion/assets/105755292/72d87eee-cafb-466d-921d-cfbfff2d53b9)



## Script Overview

The Python script named `image_processing.py` reads images from the `input_folder`, undistorts, rotates, draws a grid, and saves them in the `output_folder`.

Feel free to explore, modify and use the code for your projects.

# Perspective Transformation with OpenCV

This Python script, leveraging the OpenCV library, enables users to interactively select four points on an image and apply a perspective transformation to obtain a corrected or transformed view of the selected quadrilateral.

## How It Works
1. The user is prompted to select four points on the displayed image by clicking on it. Each click draws a small circle representing a selected point, and the coordinates of this point are printed to the console.
2. Upon the selection of four points, the script calculates the perspective transformation matrix from the selected points.
3. The script then utilizes this matrix to warp the image and simultaneously displays the original and the transformed images.

## Usage
1. Replace the image path in `cv2.imread("../corrected.JPG")` with the path of your desired image.
2. Run the script and click on four points on the displayed image to select the region you intend to transform.
3. After the fourth point is selected, observe the original and the transformed images displayed side by side.
