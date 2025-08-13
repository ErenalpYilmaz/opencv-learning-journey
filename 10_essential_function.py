import cv2 as cv
import os

# Get the current working directory
root = os.getcwd()

# Build the path to the image
imgPath = os.path.join(root, 'images/view.jpg')

# Read the image from the specified path
img = cv.imread(imgPath)

# Display the original image
cv.imshow('View', img)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray View', gray)

# Apply Gaussian blur to reduce noise and smooth the image
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Detect edges using the Canny edge detection algorithm
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilate the edges to make them thicker
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Erode the dilated image to thin the edges back
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize the image to 500x500 pixels using cubic interpolation
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Crop a specific region of the image (y1:y2, x1:x2)
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
