#Import Numpy & OpenCV(OpenCV: - V.3.4.0)
import numpy as np
import cv2


cap = cv2.VideoCapture(0) #Set Webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #Set Resolution Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) #Set Resolution Heigh
cap.set(cv2.CAP_PROP_FPS, 10) #Set Frames Per Second Rate

count = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite("frame%d.jpg" % count, frame)
    count += 1
   

    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When over, release capture and exit
cap.release()
cv2.destroyAllWindows()
