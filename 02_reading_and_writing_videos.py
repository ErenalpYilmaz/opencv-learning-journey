import cv2 as cv
import os

def videoFromWebcam():
    # Initialize video capture object with default webcam (index 0)
    # You can use 0, 1, 2, 3 for different cameras or provide a video file path
    cap = cv.VideoCapture(0)
    
    # Check if the webcam opened successfully
    if not cap.isOpened():
        exit()
    
    while True:
        # Read frame-by-frame from the webcam
        ret, frame = cap.read()
        
        # If frame reading is successful, display the frame
        if ret:
            cv.imshow("Webcam", frame)

        # Wait for 1ms and break the loop if 'q' key is pressed
        if cv.waitKey(1) == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'videos/surf.mp4')
    cap = cv.VideoCapture(vidPath)
    
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video',frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord("q"):
            break

def writeVideoToFile():
    # Initialize video capture object with default webcam (index 0)
    # You can use 0, 1, 2, 3 for different cameras or provide a video file path
    cap = cv.VideoCapture(0)
    
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    
    # Get current working directory and set output file path
    root = os.getcwd()
    outPath = os.path.join(root, 'videos/webcam.avi')
    
    # Create VideoWriter object with output path, codec, frame rate and frame size
    out = cv.VideoWriter(outPath, fourcc, 20.0, (640, 480))
    
    while cap.isOpened():
        # Read frame-by-frame from the webcam
        ret, frame = cap.read()
        
        # If frame reading is successful, write frame to output file and display it
        if ret:
            out.write(frame)           # Write the frame to the output video file
            cv.imshow("Webcam", frame) # Display the frame in a window

        # Wait for 1ms and break the loop if 'q' key is pressed
        if cv.waitKey(1) == ord('q'):
            break

    # Release the webcam, video writer and close all OpenCV windows
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    videoFromWebcam()
    videoFromFile()
    writeVideoToFile()