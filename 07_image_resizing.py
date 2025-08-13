import cv2 as cv
import os
import matplotlib.pyplot as plt

# This function loads an image, crops a small region from it, and shows how different
# OpenCV interpolation methods affect the result when that crop is resized smaller.
def imageResize():
    # Get the current working directory (folder where the script runs).
    root = os.getcwd()
    # Build the path to the image file (expects a folder named 'images' with 'cat.jpg' inside).
    imgPath = os.path.join(root,'images/cat.jpg')

    # Read the image file from disk.
    # Note: cv.imread returns images in BGR color order by default (Blue, Green, Red).
    img = cv.imread(imgPath)

    # Convert the image from OpenCV's BGR format to RGB so it displays correctly with matplotlib.
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Crop a small rectangular region from the image.
    # The indexing is [y1:y2, x1:x2, channels].
    # This takes rows 255..279 and cols 110..144 (inclusive of start, exclusive of end).
    img = img[255:280, 110:145 , :]

    # Get the height and width (number of rows and columns) of the cropped image.
    height, width,_ = img.shape

    # We will scale the cropped image down to 1/4 of its original size.
    scale = 1/4

    # A list of OpenCV interpolation flags to compare.
    # Interpolation is the method used to calculate pixel values when changing image size.
    interpMethods = [
        cv.INTER_AREA,     # Good for shrinking images — uses pixel area relation.
        cv.INTER_LINEAR,   # Bilinear interpolation — good default for resizing.
        cv.INTER_NEAREST,  # Nearest neighbor — fastest, produces blocky / pixelated results.
        cv.INTER_CUBIC,    # Bicubic interpolation — smoother than linear, slower.
        cv.INTER_LANCZOS4  # Lanczos interpolation — high-quality, slower, good for downsizing.
    ]

    # Human-readable labels for each interpolation method used above.
    interpTitle = ['area','linear','nearest','cubic','lanczos']

    # Start a new figure for plotting the images.
    plt.figure()
    # Show the original cropped image in the first subplot (position 1 of a 2x3 grid).
    plt.subplot(2,3,1)
    plt.imshow(img)
    # We do not set a title for the original so it's clear which one is the source.

    # Loop through the interpolation methods, resize the image with each method,
    # and show the result in its own subplot.
    for i in range(len(interpMethods)):
        plt.subplot(2,3,i+2)  # remaining 5 slots in the 2x3 grid
        # cv.resize expects the new size as (width, height) in pixels (integers).
        imgResize = cv.resize(
            img,
            (int(width*scale), int(height*scale)),
            interpolation=interpMethods[i]
        )
        # Display the resized image and add a title showing the interpolation type.
        plt.imshow(imgResize)
        plt.title(interpTitle[i])

    # Render the figure window with all subplots.
    plt.show()

# This standard Python idiom makes sure imageResize() runs only when the script is executed
# directly (not when it is imported as a module from another script).
if __name__ == '__main__':
    imageResize()
