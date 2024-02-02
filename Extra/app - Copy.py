# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 04:30:21 2023

@author: Administrator
"""
import cv2
import ffmpeg
import os
import cv2
import streamlit as st
import tempfile
from detect8 import detect 
import tempfile
import time
from videoprops import get_video_properties

def main():
  st.title('Omani Car plate detection and recognition Dashboard')
  st.sidebar.title('Settings')

  st.markdown(
    """
    <style>
    [data-testid="stSidebar][aria-expands='true']> div:first-child{width: 488px;}
    [data-testid="stSidebar][aria-expands='false']> div:first-child{width: -488px;}
    </style>
    """,
    unsafe_allow_html=True,
  )
  st.sidebar.markdown('-----')
  #confidence = st.sidebar.slider('Confidence', min_value=0.0, max_value=1.0, value=0.25)
 # st.sidebar.markdown('-----')
  
  #upload files
  f = st.sidebar.file_uploader('Upload an image', type=['jpg','png'])
  if f is not None:
    fo = tempfile.NamedTemporaryFile(suffix=".jpg",delete=False)
    fo.write(f.read())
    demo= open(fo.name,'rb')
    demo_b= demo.read()
    st.image(demo_b)
    h =fo.name
    m=detect(h)
    st.image(m)
    #st.image(m)

  j = st.sidebar.file_uploader('Upload an image', type=['mp4'])
  if j is not None:
    fo = tempfile.NamedTemporaryFile(suffix=".mp4",delete=False)
    fo.write(j.read())
    demo= open(fo.name,'rb')
    demo_b= demo.read()
    #st.video(demo_b)
    h =fo.name
    #m = detect(h)
    
    k ="C:/Users/Administrator/yolov7/runs/detect/exp63/IMG_6241.mp4"

    props = get_video_properties(k)               
    #demo= open("C:/Users/Administrator/yolov7/runs/detect/exp63/IMG_6241.mp4",'rb')
    #os.system("ffmpeg -i C:/Users/Administrator/yolov7/runs/detect/exp63/IMG_6241.mp4 -vcodec libx264 -f mp4  C:/Users/Administrator/yolov7/output.mp4")
    #demo= open("output.mp4")
    
    #ff = tempfile.NamedTemporaryFile(suffix=".mp4",delete=False)
    #ff.write(k.read())
    demo= open(k,'rb')
    demo_b= demo.read()
    st.video(demo_b)
    #if m is not None:

    
    
    #st.image(m)
   
  #print('kk',image_file_buffer)
  
  #displaying the image on streamlit app


  #display
  #st.video('https://youtu.be/wyWmWaXapmI')

  #st.set_option('deprecation.showfileUploaderEncoding', False)

#------------------------------------
  stframe = st.empty
  video_file_buffer = st.sidebar.file_uploader('Upload a video', type=['mp4','mov'])
  tffile = tempfile.NamedTemporaryFile(delete=False)
  use_webcam = st.sidebar.button('Use Webcam')

  if not video_file_buffer:
    if use_webcam:
      vid = cv2.VideoCapture(0)




if __name__ == '__main__':
  try:
    main()
  except SystemExit:
    pass

#streamlit run c:\users\administrator\yolov7\app.py
