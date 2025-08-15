import cv2 as cv
import numpy as np

# Read the image from the given path
img = cv.imread('images/little-cat.jpg')
cv.imshow('Little Cat', img)

# Create a completely black image (same size as original)
# This is useful for drawing shapes or results on top later
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Convert the image from color (BGR) to grayscale
# This removes color information, leaving only brightness
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Apply Gaussian blur to reduce noise and details
# (5,5) is the size of the blur window — larger means stronger blur
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Detect edges in the blurred image using Canny edge detection
# 125 = lower threshold, 175 = upper threshold for edge detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Create a binary (black and white) image from grayscale
# Pixels brighter than 125 → white (255), otherwise black (0)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Find contours (continuous lines/boundaries) in the threshold image
# cv.RETR_LIST = retrieve all contours
# cv.CHAIN_APPROX_SIMPLE = compress horizontal/vertical points for efficiency
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')

# Draw all found contours onto the blank image in red color (0,0,255)
# Thickness = 1 pixel
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

# Wait indefinitely for a key press before closing windows
cv.waitKey(0)
