#import tkinter as tk
from tkinter import *
from tkinter import font
from tkVideoPlayer import TkinterVideo
from tkinter.filedialog import askopenfile
from detect8 import detect 
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()

window.title("Tkinter Advanced Video Player")

window.geometry ("500x500")

window.configure(bg="yellow")

lbl1 = Label(window, text="LPR System", bg="yellow" ,fg="black", font="none 24 bold")

lbl1.pack(side=TOP, pady=2)

def upload_video():
    file = askopenfile(mode="r", filetypes=[('Video Files',['*.mp4',"*.mov",'*.jpg'])])
    if file is not None:
        global filename
        filename = file.name
        VD = detect(filename)
        global videoplayer
        videoplayer = TkinterVideo(master=window, scaled=True)
        videoplayer.load(r"{}".format(VD) )
        videoplayer.pack()
        videoplayer.play()

def upload_images():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    IFile = filedialog.askopenfilename(filetypes=f_types)
    if IFile is not None:
        ID = detect(IFile)
        print("ID IS ", ID)
        img = ImageTk.PhotoImage(file=ID)
        b2 =Label(image=img) # using Button
        b2.pack()
    #img.pack(expand=True, fill="both")

#image button    
Imgbtn = Button(window, text="Upload image" , command=lambda:upload_images())
Imgbtn.pack()

#video button
Vibtn = Button(window, text="Upload Video" , command=lambda:upload_video())
Vibtn.pack()

window.mainloop()



