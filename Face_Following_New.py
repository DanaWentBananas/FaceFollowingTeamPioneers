'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

import numpy as np
import cv2
import imutils
import functions as f

import RPi.GPIO as GPIO          
from time import sleep
from time import sleep as wait

in1 = 24
in2 = 23
in3 = 19
in4 = 26
enA = 25
enB = 13
temp1=1
x=y=w=h=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(enA,1000)
p2=GPIO.PWM(enB,1000)
p1.start(17)
p2.start(17)

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height


while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (70, 70))
#     img = imutils.resize(frame, width=400)
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x=y=w=h=0
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #print("x: ", x, "y: ", y, "w: ", w, "h: ", h)
        print("x")
        
#     Mx = w/2
#     My = h/2
#     
#     
#     if Mx < 30 and x > 0:
#         GPIO.output(in1,GPIO.HIGH)
#         GPIO.output(in2,GPIO.LOW) 
#         GPIO.output(in3,GPIO.LOW)
#         GPIO.output(in4,GPIO.HIGH)
#          
#     elif x > 70 :
# #          
#         GPIO.output(in1,GPIO.LOW)
#         GPIO.output(in2,GPIO.HIGH)
#         GPIO.output(in3,GPIO.HIGH)
#         GPIO.output(in4,GPIO.LOW)
    
#     elif x == w/2 and y == h/2:
#        GPIO.output(in1,GPIO.LOW)
#        GPIO.output(in2,GPIO.LOW)
#        GPIO.output(in3,GPIO.LOW)
#        GPIO.output(in4,GPIO.LOW)
    
    else:
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in2,GPIO.LOW)
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in4,GPIO.LOW)
    
    print("the area is:",w*h)
    
     
    if w*h < 1025 and w*h > 950 or w*h==0:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

#         
#         
     
    elif w*h > 1025:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        
    elif w*h < 950:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

         
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        break
        
        

cap.release()
cv2.destroyAllWindows()