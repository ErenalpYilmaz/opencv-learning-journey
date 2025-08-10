import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# load a color image
img = cv.imread('images/cat.jpg')
assert img is not None, "File could not be read, check with os.path.exists()"

"""
    Access a pixel value by its row and column coordinates
    for BGR images. 
    B: Blue
    G: Green
    R: Red
"""
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100, 100, 0]
print(blue)

# modify the pixel values
img[100, 100] = [255, 255, 255]
print(img[100,100])

# rows, column, channels
# height, width, channels
print( f"Img shape: {img.shape }") 
#-> image = 1280x853

# Total number of pixels.
# height x width x channels
print(f"Img size: {img.size}")

# type
print(f'Img dtype: {img.dtype }')

"""
Copy the coordinates of the ball in the image and paste them into the coordinates of the location where you want to place the ball.
"""
# img2 = cv.imread("images/messi.jpg")
# ball = img2[280:340, 330:390]
# img2[273:333,100:160] = ball
#example -> images/messi.jpg

b, g, r = cv.split(img)
img = cv.merge((b,g,r))
print(img)


BLUE = [255,0,0]
 
img1 = cv.imread('images/woman.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
 
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
 
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
 
plt.show()
