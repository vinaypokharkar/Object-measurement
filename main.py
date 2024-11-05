import cv2
import numpy as np
import utlis
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Parameters for scaling and paper dimensions
scale = 3
wP = 210 * scale
hP = 297 * scale

# Variable to store the selected image path
selected_image_path = None

# Function to browse files
def browse_files():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if selected_image_path:
        process_image(selected_image_path)

# Function to process the selected image
def process_image(path):
    img = cv2.imread(path)

    # Resize the image to 1080x1920
    img_resized = cv2.resize(img, (1080, 1920))

    img_resized, conts = utlis.getContours(img_resized, showCanny=False, minArea=50000, filter=4, draw=True)

    if len(conts) != 0:
        biggest = conts[0][2]
        imgWarp = utlis.warpImg(img_resized, biggest, wP, hP)

        img2, conts2 = utlis.getContours(imgWarp, showCanny=False, minArea=2000, filter=4, draw=False, cThr=[50, 50])

        if len(conts2) != 0:
            for obj in conts2:
                cv2.polylines(img2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = utlis.reorder(obj[2])
                nW = round((utlis.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale) / 10), 1)
                nH = round((utlis.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10), 1)

                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(img2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)

        # Display the processed image in a new OpenCV window
        cv2.imshow('Warped Image', img2)

    # Display the original image (resized to 1080x1920) in another OpenCV window
    # cv2.imshow('Original', img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Tkinter window setup
root = tk.Tk()
root.title("Image File Browser")
root.geometry("300x150")

# Browse button
browse_button = tk.Button(root, text="Browse Image", command=browse_files)
browse_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
