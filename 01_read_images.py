import cv2 as cv

# Reading image.
img = cv.imread('images/woman.jpg')

# Image resize
resized_img = cv.resize(img, (0,0), fx=0.5 , fy=0.5)

#display images the new window
cv.imshow("Woman", resized_img)

cv.waitKey(0)