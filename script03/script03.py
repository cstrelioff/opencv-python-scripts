#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
script03.py

Adding command line argprase to script that does video capture and writing 
video files on Pop_OS! (Ubuntu) 22.04 operating system.

Following documentation at:
https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

"""
import numpy as np
import cv2

#
# command line argument processing
#
import argparse
parser = argparse.ArgumentParser(prog='./opencv-video-edge-detection.py')
# save a video file?
parser.add_argument('-s', '--save', help='save a video file', dest='save', action='store_true')
# assign a file name, default is video.mp4
parser.add_argument('-f', '--file', help='filename for video, should be mp4', dest='file', default='video.mp4')
# parse arguments & provide message at terminal
args = parser.parse_args()
if (args.save == True):
    print(f'...saving video to {args.file}.')
else:
    print('...not saving video to file.')
print('Hit "q" to quit.')

# pass argument 0 for device index (1st camera)
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

# create VideoWrite if -s or --save flags passed
if (args.save):
    # create VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # using file name in args.file
    output = cv2.VideoWriter(args.file, fourcc, 20.0, (width, height), isColor)

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

    if (args.save):
        # write to the output is -s or --save flag passed
        output.write(gray_frame)
    
    # listen for 'q' press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# everything done
# - release capture
# - release video writer
# - destroy all windows
vcap.release()

if (args.save):
    # run is -s or --save flags passed
    output.release()

cv2.destroyAllWindows()
