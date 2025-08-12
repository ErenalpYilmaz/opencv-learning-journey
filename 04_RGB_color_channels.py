import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def pureColors():
    # Create a 100x100 array filled with zeros (black pixel values)
    zeros = np.zeros((100, 100))
    
    # Create a 100x100 array filled with ones (will later become white when multiplied by 255)
    ones = np.ones((100, 100))
    
    # Create a solid blue image: (Blue channel = 255, Green = 0, Red = 0)
    bImg = cv.merge((zeros, zeros, 255 * ones))
    
    # Create a solid green image: (Blue = 0, Green = 255, Red = 0)
    gImg = cv.merge((zeros, 255 * ones, zeros))
    
    # Create a solid red image: (Blue = 0, Green = 0, Red = 255)
    rImg = cv.merge((255 * ones, zeros, zeros))
    
    # Create a black image: (Blue = 0, Green = 0, Red = 0)
    blackImg = cv.merge((zeros, zeros, zeros))
    
    # Create a white image: (Blue = 255, Green = 255, Red = 255)
    whiteImg = cv.merge((255 * ones, 255 * ones, 255 * ones))
    
    # Start plotting the images in a single figure
    plt.figure()
    
    # Show the blue image
    plt.subplot(231)  # Position: row 2, col 3, index 1
    plt.imshow(bImg.astype(np.uint8))  # Convert to integer values for display
    plt.title("Blue")
    
    # Show the green image
    plt.subplot(232)
    plt.imshow(gImg.astype(np.uint8))
    plt.title("Green")
    
    # Show the red image
    plt.subplot(233)
    plt.imshow(rImg.astype(np.uint8))
    plt.title("Red")
    
    # Show the black image
    plt.subplot(234)
    plt.imshow(blackImg.astype(np.uint8))
    plt.title("Black")
    
    # Show the white image
    plt.subplot(235)
    plt.imshow(whiteImg.astype(np.uint8))
    plt.title("White")
    
    # Display all the images together
    plt.show()

    
    
def bgrChannelGrayScale():
    # Get the current working directory (folder where this script is running)
    root = os.getcwd()
    
    # Create the full path to the image file (images/woman.jpg inside the current folder)
    imgPath = os.path.join(root, 'images/woman.jpg')
    
    # Read the image using OpenCV (this loads it in BGR color format by default)
    img = cv.imread(imgPath)
    
    # Split the image into its three color channels: Blue, Green, and Red
    # Each channel is a grayscale image showing the intensity of that color
    b, g, r = cv.split(img)
    
    # If we wanted to create a zero-filled channel (completely black),
    # we could use this (currently commented out):
    # zeros = np.zeros_like(b)
    
    # Start a new figure for displaying the results
    plt.figure()
    
    # Show the Blue channel in grayscale
    plt.subplot(131)               # 1 row, 3 columns, first image
    plt.imshow(b, cmap='gray')     # Show as black & white image
    plt.title("Blue Channel")
    
    # Show the Green channel in grayscale
    plt.subplot(132)               # Second image in the row
    plt.imshow(g, cmap='gray')
    plt.title("Green Channel")
    
    # Show the Red channel in grayscale
    plt.subplot(133)               # Third image in the row
    plt.imshow(r, cmap='gray')
    plt.title("Red Channel")
    
    # Display all the subplots
    plt.show()

    

def bgrChannelColor():
    # Get the current working directory (where this script is running)
    root = os.getcwd()
    
    # Create the full file path to the image "images/sky.jpg"
    imgPath = os.path.join(root, 'images/sky.jpg')
    
    # Read the image using OpenCV (loads it in BGR format: Blue, Green, Red)
    img = cv.imread(imgPath)
    
    # Split the image into its three color channels
    # b = Blue channel, g = Green channel, r = Red channel
    b, g, r = cv.split(img)
    
    # Create a zero-filled array (completely black) with the same size as one channel
    zeros = np.zeros_like(b)
    
    # Create an image showing only the Blue channel in color
    # Blue stays as it is, Green and Red channels are set to 0 (black)
    bImg = cv.merge((b, zeros, zeros))
    
    # Create an image showing only the Green channel in color
    gImg = cv.merge((zeros, g, zeros))
    
    # Create an image showing only the Red channel in color
    rImg = cv.merge((zeros, zeros, r))
    
    # Start plotting the images
    plt.figure()
    
    # Show the Blue channel image
    plt.subplot(131)               # 1 row, 3 columns, first position
    plt.imshow(bImg)
    plt.title("Blue Channel")
    
    # Show the Green channel image
    plt.subplot(132)               # Second position
    plt.imshow(gImg)
    plt.title("Green Channel")
    
    # Show the Red channel image
    plt.subplot(133)               # Third position
    plt.imshow(rImg)
    plt.title("Red Channel")
    
    # Display all three images
    plt.show()

    
    

if __name__ == '__main__':
    pureColors()
    bgrChannelGrayScale()
    bgrChannelColor()