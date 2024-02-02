# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:05:10 2023

@author: Administrator
"""
from detect8 import detect
detect("C:/Users/Administrator/yolov7/inference/images", "best.pt", view_img=True, save_txt=True, trace=True,nosave=True,save_img=False,webcam=False,device="cpu", imgsZ=512,augment=True,conf=0.5,iou_thres=0.45,save_conf=True)