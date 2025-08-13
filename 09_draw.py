import cv2 as cv
import numpy as np
import os

# Create a blank image (400x400) with 3 color channels (BGR), filled with zeros (black)
blank = np.zeros((400, 400, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Get the current working directory
root = os.getcwd()
# Create the path to the sample image
imgPath = os.path.join(root, 'images/view.jpg')
# Read the sample image from the path
img = cv.imread(imgPath)

# Display the original image
cv.imshow('View', img)

# -----------------------------------------------------
# 1. Paint the image a certain color (example commented out)
# This would fill a rectangular region in the blank image with green
blank[150:250, 160:260] = 0, 255, 0
cv.imshow('Green', blank)

# -----------------------------------------------------
# 2. Draw a filled rectangle
# thickness = -1 means the rectangle will be filled
cv.rectangle(blank, (100, 100), (250, 300), (0, 255, 0), thickness=-1) 
cv.imshow('Rectangle', blank)

# Example: Rectangle from a point to half the width/height of the image (commented out)
cv.rectangle(blank, (100,100), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# -----------------------------------------------------
# 3. Draw a filled circle
# Center: middle of the image, radius: 40 pixels, color: red, filled
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('circle', blank)

# -----------------------------------------------------
# 4. Draw a white line
# From point (100, 250) to point (200, 300), thickness: 3
cv.line(blank, (100, 250), (200, 300), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# -----------------------------------------------------
# 5. Write text on the image
# Text: "Hello my name is ALP!", position: (100, 80), font: Hershey Triplex,
# scale: 0.5, color: green, thickness: 1
cv.putText(blank, 'Hello my name is ALP!', (100, 80), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), thickness=1)
cv.imshow('Text', blank)

# Final display of the image with all shapes and text
cv.imshow('Rectangle', blank)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
