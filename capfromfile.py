
#Import Numpy & OpenCV (OpenCV :- V.3.4.0)
import cv2

cap=cv2.VideoCapture('MOV00023.3gp') #Set Video File name
cap.set(cv2.CAP_PROP_FPS, 10) #Set Frames Per Second Rate

success,image = cap.read()
count = 0
success = True
while success:
  cv2.imwrite("data/frame%d.jpg" % count, cv2.resize(image, (320, 240)))  #Save frame as JPEG file as per resolution
  success,image = cap.read()
  print('Read a new frame: ', success)
  count += 1
