import cv2 as cv
import os

# Function to rescale images or video frames by a given scale factor
def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos, and Live Video
    width = int(frame.shape[1] * scale)   # New width based on scale
    height = int(frame.shape[0] * scale)  # New height based on scale
    dimensions = (width, height)          # Dimensions tuple
    
    # Resize the frame using interpolation for better quality
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    

# Function to change resolution for live video capture
def changeRes(width, height):
    # Only works for live video (webcam)
    capture.set(3, width)   # Property 3 → width
    capture.set(4, height)  # Property 4 → height
    

# Get the current working directory
root = os.getcwd()
# Create the path to the image file
imgPath = os.path.join(root, 'images/view.jpg')

# Read the image from the given path
img = cv.imread(imgPath)
# Display the original image
cv.imshow('try', img)

# Resize the image using the rescaleFrame function
resized_image = rescaleFrame(img)
# Display the resized image
cv.imshow('resized image', resized_image)

# Open the video file for reading
capture = cv.VideoCapture('videos/surf.mp4')

# Loop to read and display each frame
while True:
    isTrue, frame = capture.read()  # Read a frame from the video
    
    # Resize the frame to 30% of its original size
    frame_resized = rescaleFrame(frame, .3)
    
    # Display the original video frame
    cv.imshow("Video", frame)
    # Display the resized video frame
    cv.imshow('Video Resized', frame_resized)
    
    # If 'q' key is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release video capture object
capture.release()
# Close all OpenCV windows
cv.destroyAllWindows()
