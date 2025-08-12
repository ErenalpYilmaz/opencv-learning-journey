import cv2 as cv
import os 

"""
#? Why do we need grayscale images?
-> Grayscale images use less data compared to color images, which makes processing faster.
Many image processing tasks, like edge detection, only need brightness information, not color.
Grayscale pixel value is calculated by combining the red, green, and blue channels:
Grayscale Pixel = 0.299*R + 0.587*G + 0.114*B
"""

def grayScale():
    # Get current working directory
    root = os.getcwd()
    # Build the path to the image file
    imgPath = os.path.join(root, 'images/woman.jpg')
    # Read the image in color (default)
    img = cv.imread(imgPath)
    # Reduce the image size to half for faster processing and display
    resized_img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    # Convert the resized color image to grayscale (black & white)
    imgGray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
    
    # Show the grayscale image in a window titled "Grey"
    cv.imshow("Grey", imgGray)
    # Wait for a key press to close the window
    cv.waitKey(0)

def readAsGrey():
    # Get current working directory
    root = os.getcwd()
    # Build the path to the image file
    imgPath = os.path.join(root, 'images/woman.jpg')
    # Read the image directly as grayscale (without color)
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    # Reduce the image size to half for faster processing and display
    resized_img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    
    # Show the grayscale image in a window titled "gray"
    cv.imshow("gray", resized_img)
    # Wait for a key press to close the window
    cv.waitKey(0)


if __name__ == "__main__":
    grayScale()    # Convert a color image to grayscale after loading
    readAsGrey()    # Load image directly as grayscale
