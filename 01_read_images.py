import cv2 as cv
import os
"""
    Pixel Range
    8 bit representation
    2^8 = 256
    Min: 0 (Black)
    Max: 255 (White)
    
    BGR Pixel
    Blue - Green - Red [B, G, R]
    
    ----------------------------------
    
    Image Dimension
    
    Dim:(M, N, 3)
    M - Height, y
    N - Width, x
"""

def readImage():
    # Get the current working directory
    root = os.getcwd()
    
    # Create the full path of the cat.jpg file in the image folder.
    imgPath = os.path.join(root, 'images/cat.jpg')
    
    # Reading image.
    img = cv.imread(imgPath)
    
    # Image resize
    resized_img = cv.resize(img, (0,0), fx=0.5 , fy=0.5)
    
    #display images the new window
    cv.imshow("Woman", resized_img)
    
    cv.waitKey(0)

def writeImage():
     # Get the current working directory
    root = os.getcwd()
    
    # Create the full path of the cat.jpg file in the image folder.
    imgPath = os.path.join(root, 'images/cat.jpg')
    
    # Reading image.
    img = cv.imread(imgPath)
    
    #Create the full path of the output.jpg file in the image folder.
    outPath = os.path.join(root, 'images/output.jpg')

    #Write new images this path
    cv.imwrite(outPath,img)
    
    
if __name__ == "__main__":
    readImage()
    writeImage()









