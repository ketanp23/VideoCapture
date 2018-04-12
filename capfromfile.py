
#Import Numpy & OpenCV (OpenCV :- V.3.4.0)
import numpy as np
import cv2



cap=cv2.VideoCapture('MOV00023.3gp') #Set Video File name
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #Set Resolution Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) #Set Resolution Height
cap.set(cv2.CAP_PROP_FPS, 10) #Set Frames Per Second Rate

success,image = cap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image) #Save frame as JPEG file
  success,image = cap.read()
  print('Read a new frame: ', success)
  count += 1
