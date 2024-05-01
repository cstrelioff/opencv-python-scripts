#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
script02.py

Testing video capture and writing files on Pop_OS! (Ubuntu) 22.04 
operating system.

Following documentation at:
https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

"""
import numpy as np
import cv2

# pass argument 0 for device index (hopefully laptop cam)
vcap = cv2.VideoCapture(0);
if not vcap.isOpened():
    print("Can't open camera!")
    exit()

# get height and width of capture
width = int(vcap.get(3))
height = int(vcap.get(4))

# bool for isColor is optional, BUT defaults to True!
# - doing grayscale in the loop, so have to set to false!
isColor = False

# create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('video.mp4', fourcc, 20.0, (width, height), isColor)

# loop until
# - error reading frame from camera
# - or, user hits 'q'
while True:
    # read a frame
    ret, frame = vcap.read();

    # ret == True if frame read correctly
    if not ret:
        print("Can't read frame, exiting...")
        break

    # process frame
    # - change BGR -> GRAY (video should be grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display resulting fram
    cv2.imshow('frame', gray_frame)

    # write to the output
    output.write(gray_frame)
    
    # listen for 'q' press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# everything done
# - release capture
# - release video writer
# - destroy all windows
vcap.release()
output.release()
cv2.destroyAllWindows()
