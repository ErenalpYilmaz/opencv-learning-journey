import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

"""
# Why do we need the HSV color space?
# HSV separates color into three components: Hue, Saturation, and Value.
# This separation makes it easier to adjust colors and is less sensitive to lighting changes.
# It is especially useful in image processing and computer vision tasks.

H: Hue (0-180, typically 0-360)
    Type of color

S: Saturation (0-255)
    Concentration of the color

V: Value (0-255)
    Intensity of the color
"""

def hsvColorSegmentation():
    # Get the current working directory
    root = os.getcwd()
    
    # Create the full path to the image file
    imgPath = os.path.join(root, 'images/woman.jpg')
    
    # Load the image in BGR color space (default in OpenCV)
    img = cv.imread(imgPath)
    
    # Resize the image to half of its original size for faster processing and display
    resized_img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    
    # Convert the BGR image to RGB color space for correct color display with matplotlib
    imgRGB = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    
    # Convert the resized image from BGR to HSV color space for color segmentation
    hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)
    
    # Define the lower and upper bounds for the color to segment (Hue, Saturation, Value)
    lowerBound = np.array([0, 0, 50])
    upperBound = np.array([10, 120, 100])
    
    # Create a mask that highlights pixels within the specified HSV range
    mask = cv.inRange(hsv, lowerBound, upperb=upperBound)  # Note: 'upperb=' is a typo; should be 'upperb=upperBound' or simply upperBound
    
    # Display the original image using matplotlib
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    
    # Show the mask result in a separate window
    cv.imshow('mask', mask)
    
    # Wait indefinitely until a key is pressed, then close windows
    cv.waitKey(0)
    
if __name__ == '__main__':
    hsvColorSegmentation()