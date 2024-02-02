# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:08:56 2023

@author: Administrator
"""
import cv2
import subprocess

import subprocess


k ="C:/Users/Administrator/yolov7/inference/video/IMG_6241.mp4"
h="C:/Users/Administrator/yolov7/runs/detect/exp63/IMG_6241.mp4"

subprocess.call(args=f"ffmpeg -y -i {k} -c:v libx264 {h}".split(" "))
    
#k ="C:/Users/Administrator/yolov7/inference/video/IMG_6241.mp4"
#cv2.VideoWriter_fourcc(*'h264')
#props = get_video_properties(k)

