import cv2 as cv
import os
import matplotlib.pyplot as plt


def readAndWriteSinglePixel():
    # Get the current working directory
    root = os.getcwd()
    # Construct the full path to the image file
    imgPath = os.path.join(root, 'images/cat.jpg')
    
    # Read the image from disk
    img = cv.imread(imgPath)
    
    # Resize the image to half its original size
    resized_img = cv.resize(img, (0,0), fx=0.5 , fy=0.5)
    
    # Convert the image from BGR to RGB color space for correct display in matplotlib
    imgRGB = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    
    # Display the image
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    # Access the pixel value at coordinates (131, 267)
    eyePixel = imgRGB[131,267]
    
    # Change the pixel at (265, 130) to red color (R=255, G=0, B=0)
    imgRGB[265,130] = (255, 0, 0)
    
    # Display the modified image
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    
    debug = 1


def readAndWritePixelRegion():
    # Get the current working directory
    root = os.getcwd()
    # Construct the full path to the image file
    imgPath = os.path.join(root, 'images/cat.jpg')
    
    # Read the image from disk
    img = cv.imread(imgPath)
    
    # Resize the image to half its original size
    resized_img = cv.resize(img, (0,0), fx=0.5 , fy=0.5)
    
    # Convert the image from BGR to RGB color space for correct display in matplotlib
    imgRGB = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
    
    # Display the original image
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    
    # Extract a rectangular region of pixels (eye region) from the image
    eyeRegion = imgRGB[255:280, 110:145]
    
    # Calculate the height (dx) and width (dy) of the extracted region
    dx = 280 - 255
    dy = 145 - 110
    
    # Define the starting coordinates where the eyeRegion will be copied
    startX = 230
    startY = 160
    
    # Copy the eyeRegion to a new location in the image
    imgRGB[startX:startX + dx, startY: startY + dy] = eyeRegion
    
    # Display the modified image
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    
    debug = 1


if __name__ == '__main__':
    readAndWriteSinglePixel()
    readAndWritePixelRegion()
