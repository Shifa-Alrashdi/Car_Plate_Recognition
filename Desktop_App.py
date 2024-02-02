#Import  a libraries 
import tkinter
import tkinter.messagebox
import customtkinter
from tkVideoPlayer import TkinterVideo
from tkinter.filedialog import askopenfile
from detect import detect 
from PIL import Image, ImageTk
import os
from tkinter.ttk import *
import cv2


#Class to display video in a suitable size on the Customtkinter window
class vidoFrame():

    def __init__(self, window, cap):

        self.window = window

        self.cap = cap

        self.interval = 20 # Interval in ms to get the latest frame

        # Create canvas for image

        self.canvas = tkinter.Canvas(self.window,width=700,height=650)

        self.canvas.grid(row=0, column=1)

        # Update image on canvas

        self.update_image()

    def update_image(self):

        # Get the latest frame and convert image format

        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB

        self.image = Image.fromarray(self.image) # to PIL format

        self.image = self.image.resize((700,650))

        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format

        # Update image

        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.image)

        # Repeat every 'interval' ms

        self.window.after(self.interval, self.update_image)

#Initialize variables
imgFile= None
vidFile = None

#Function to upload an image
def uploadImage():

    global imgFile
    print("uploadImage click")
    
    #Delete everything displayed on the Customtkinter window
    for widgets in inputFrame.winfo_children():
      widgets.destroy()
      
    #Upload an image  
    global img
    f_types = [('Jpg Files', '*.jpg')]
    imgFile = askopenfile(filetypes=f_types)

    #Delete the uploaded video from its variable
    global vidFile
    vidFile= None
    
    if imgFile is not None:

        #Open an image 
        imgOpne = Image.open(imgFile.name)
        
        #Re-size an image
        imgResized = imgOpne.resize((700,650), Image.ANTIALIAS)
        
        #Display an image on the Customtkinter window
        img = ImageTk.PhotoImage(imgResized)
        imageLable = tkinter.Label(inputFrame,image=img) 
        imageLable.grid(row=0,column=1)

def uploadVideo():

    print("uploadVideo click")

    #Delete everything displayed on the Customtkinter window
    for widgets in inputFrame.winfo_children():
      widgets.destroy()
      
    #Upload a video
    file = askopenfile( filetypes=[('Video Files',['*.mp4',"*.mov"])])
    
    #Delete the uploaded image from its variable
    global imgFile
    imgFile= None
    
    if file is not None:
        
        #Display a video on the Customtkinter window
        global vidFile
        vidFile = file.name
        vidoFrame(inputFrame, cv2.VideoCapture(vidFile))

#function to delete everything displayed on the Customtkinter window
def cancel():
   
    global imgFile
    global vidFile
    imgFile= None
    vidFile = None
    for widgets in inputFrame.winfo_children():
      widgets.destroy()

#function to detect license car plate and recognize alphanumeric of it
def detectt():
    
    #Delete everything displayed on the Customtkinter window
    for widgets in inputFrame.winfo_children():
      widgets.destroy()
      
    global imgFile
    
    if imgFile is not None:
        
        #Detect the license car plate of an image and recognize the alphanumeric of it
        ID = detect(imgFile.name)
        
        if ID is not None:
          #Open the detected image
          imgOpne2 = Image.open(ID)
          
          #Re-size an image
          imgResized2 = imgOpne2.resize((700,650), Image.ANTIALIAS)
          
          #Display an image on the Customtkinter window
          img2 = ImageTk.PhotoImage(imgResized2)
          imageLable2 = tkinter.Label(inputFrame,image=img2) 
          imageLable2.image = img2
          imageLable2.grid(row=1,column=1)
      
    global vidFile
    
    if vidFile is not None:
        
        #Detect the license car plate of a video and recognize the alphanumeric of it
        VD = detect(vidFile)

        if VD is not None:
            
            #Display the video on the Customtkinter window
            vidoFrame(inputFrame, cv2.VideoCapture(VD))


#Determine customtkinter window design
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

#Set title for the customtkinter window
root.title("Omani Car Plate Detection and Recognition Dashboard")

#Set size for the customtkinter window
root.geometry(f"{1000}x{580}")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

#Create a frame for upload buttons on customtkinter window
sidebar_frame = customtkinter.CTkFrame(root, width=250, height=570,corner_radius=5)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_columnconfigure(0,weight=1)

#Display the text 'upload' on the frame
logo_label = customtkinter.CTkLabel(sidebar_frame, text="Upload", font=customtkinter.CTkFont(size=20, weight="bold"))

#Set the location of the text 'upload' on the frame
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

#Create an image upload button
uploadImage_button = customtkinter.CTkButton(sidebar_frame, text="Upload Image", command=uploadImage)

#Set the location of the image upload button on the frame
uploadImage_button.grid(row=1, column=0, padx=20, pady=10)

#Create a video upload button
uploadVideo_button = customtkinter.CTkButton(sidebar_frame,  text="Upload Video",command=uploadVideo)


#Set the size and location of the video upload button on the frame
uploadVideo_button.grid(row=2, column=0, padx=20, pady=10)

#Create a frame for displaying an image or video and buttons
displayframe = customtkinter.CTkFrame(root, width=800,height=570, corner_radius=5)
displayframe.grid(row=0,column=1)
displayframe.grid_rowconfigure(0,weight=2)
displayframe.grid_rowconfigure(1,weight=2)
displayframe.grid_rowconfigure(3,weight=1)

#Create a frame for displaying an image or video
inputFrame = customtkinter.CTkFrame(displayframe,width=750,height=500)
inputFrame.grid(row=0,padx=5,pady=5,columnspan=2)

#Create a cancel button 
cancel = customtkinter.CTkButton(displayframe, text="Cancel",text_color="white",command=cancel)

#Set a cancel button location
cancel.grid(row=2,column=1)

#Create a detect button 
detect2 = customtkinter.CTkButton(displayframe, text="Detect",text_color="white",command=detectt)

#Set a detect button location
detect2.grid(row=2,column=0)

root.mainloop()



