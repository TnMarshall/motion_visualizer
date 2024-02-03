import numpy as np
import cv2

vcap = cv2.VideoCapture("http://192.168.1.###:####/stream.mjpg")   # streaming from an rpi4

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)