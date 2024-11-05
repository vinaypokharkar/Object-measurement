# Image Measurement Tool

This project provides a graphical interface to upload an image and measure objects within it using OpenCV. After selecting an image, the application detects contours, warps the image, and calculates the dimensions of objects in centimeters. The application is built using Python with OpenCV for image processing, Tkinter for the GUI, and Pillow for image handling.

![Result](https://github.com/user-attachments/assets/f24f921a-83aa-4b58-ab98-a679fb044bc7)


## Features

- Upload images for processing using a simple file browser.
- Resize the uploaded image to a standardized 1080x1920 resolution.
- Detect and highlight contours of objects in the image.
- Measure object dimensions in centimeters and display them directly on the image.
- Easy-to-use GUI with buttons to select images.

## Requirements

To run this project, you need the following Python modules:

- [OpenCV](https://opencv.org/) for image processing (`cv2`).
- [NumPy](https://numpy.org/) for array operations.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical interface (included with Python).
- [Pillow](https://pillow.readthedocs.io/) for handling image files in Tkinter.
- `utlis.py` file, which should contain custom utility functions (details below).

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/image-measurement-tool.git
cd image-measurement-tool
