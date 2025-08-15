import cv2 as cv
import numpy as np

# Read the image from the file path
# 'images/view.jpg' is the file location
img = cv.imread('images/view.jpg')

# Show the original image in a window titled "Desert"
cv.imshow('Desert', img)

# ---------------- Translation (Moving the Image) ---------------- #
def translate(img, x, y):
    """
    Move the image horizontally (x) and vertically (y).
    Positive x → move right, negative x → move left.
    Positive y → move down, negative y → move up.
    """

    # Create the translation matrix:
    # 1 and 0 keep the image scale same, x and y shift it
    transMat = np.float32([[1, 0, x], [0, 1, y]])

    # Dimensions of the final image (width, height)
    dimensions = (img.shape[1], img.shape[0])

    # Apply the shift (warpAffine moves the image)
    return cv.warpAffine(img, transMat, dimensions)

# Move the image 100 pixels left and 100 pixels down
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# ---------------- Rotation (Turning the Image) ---------------- #
def rotate(img, angle, rotPoint=None):
    """
    Rotate the image by a given angle.
    Positive angle → counterclockwise rotation.
    Negative angle → clockwise rotation.
    """

    # Get the height and width of the image
    (height, width) = img.shape[:2]
    
    # If no rotation point is given, use the center of the image
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    # Create the rotation matrix:
    # rotPoint = center of rotation
    # angle = how much to rotate
    # 1.0 = scale (no zoom in or out)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Final image size after rotation
    dimensions = (width, height)
    
    # Apply the rotation
    return cv.warpAffine(img, rotMat, dimensions)

# Rotate the image 45 degrees clockwise
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Rotate the already rotated image another 90 degrees clockwise
rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# ---------------- Resizing (Changing Image Size) ---------------- #
# Resize the image to 500x500 pixels
# INTER_CUBIC = better quality for enlarging images
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# ---------------- Flipping (Mirroring the Image) ---------------- #
# flipCode:
#  0  → flip vertically (upside down)
#  1  → flip horizontally (mirror left-right)
# -1  → flip both vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# ---------------- Cropping (Cutting Out Part of the Image) ---------------- #
# Keep only the part of the image from y=200 to y=400
# and from x=300 to x=400 (this is like cutting a rectangle out)
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

# Wait for a key press before closing all windows
cv.waitKey(0)
