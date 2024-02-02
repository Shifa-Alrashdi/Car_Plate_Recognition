import tkinter

import tkinter.messagebox

import customtkinter

from tkVideoPlayer import TkinterVideo

from tkinter.filedialog import askopenfile

from detect8 import detect 

from PIL import Image, ImageTk

import os





def uploadImage():

    print("uploadImage click")

    global img

    f_types = [('Jpg Files', '*.jpg')]

    imgFile = askopenfile(filetypes=f_types)
    
   

    if imgFile is not None:
        
        img = ImageTk.PhotoImage(file=imgFile.name)

        imageLable = tkinter.Label(input,image=img,width=700,height=200) 

        imageLable.grid(row=0,column=1)
        
        #Detection
        ID = detect(imgFile.name)
        
       
        img = ImageTk.PhotoImage(file=ID)

        imageLable0 = tkinter.Label(output,image=img,width=700,height=200) 

        imageLable0.grid(row=1,column=1)

        



def uploadVideo():

    print("uploadVideo click")

    file = askopenfile( filetypes=[('Video Files',['*.mp4',"*.mov",'*.jpg'])])

    if file is not None:

        global filename

        filename = file.name

        global videoplayer

        videoplayer = TkinterVideo( scaled=True,master=input)

        videoplayer.load(r"{}".format(file.name) )

        videoplayer.pack()

        videoplayer.grid(row=0,column=1,padx=5,pady=5)

        videoplayer.play()



        

        VD = detect(filename)

        if VD is not None:

            videoplayer = TkinterVideo(master=output, scaled=True)

            videoplayer.load(r"{}".format(VD) )

            videoplayer.pack()

            videoplayer.grid(row=1,column=1,padx=5,pady=5)

            videoplayer.play()

        



def cancel():

    for widgets in input.winfo_children():

      widgets.destroy()

    

    for widgets in output.winfo_children():

      widgets.destroy()



customtkinter.set_appearance_mode("Dark")

customtkinter.set_default_color_theme("dark-blue")



root = customtkinter.CTk()

root.title("Omani Car Plate Detection and Recognition Dashboard")

root.geometry(f"{1000}x{580}")



root.grid_columnconfigure(0, weight=1)

root.grid_columnconfigure(1, weight=3)



sidebar_frame = customtkinter.CTkFrame(root, width=250, height=570,corner_radius=5)

sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

sidebar_frame.grid_columnconfigure(0,weight=1)



logo_label = customtkinter.CTkLabel(sidebar_frame, text="Uploadation", font=customtkinter.CTkFont(size=20, weight="bold"))

logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))



uploadImage_button = customtkinter.CTkButton(sidebar_frame, text="Upload Image", command=uploadImage)

uploadImage_button.grid(row=1, column=0, padx=20, pady=10)



uploadVideo_button = customtkinter.CTkButton(sidebar_frame,  text="Upload Video",command=uploadVideo)

uploadVideo_button.grid(row=2, column=0, padx=20, pady=10)



displayframe = customtkinter.CTkFrame(root, width=800,height=570, corner_radius=5)

displayframe.grid(row=0,column=1)

displayframe.grid_rowconfigure(0,weight=2)

displayframe.grid_rowconfigure(1,weight=2)

displayframe.grid_rowconfigure(3,weight=1)



#image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")

#image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))



input = customtkinter.CTkFrame(displayframe,width=750,height=260,)

input.grid(row=0,column=1,padx=5,pady=5)





output = customtkinter.CTkFrame(displayframe,width=750,height=260)

output.grid(row=1,column=1,padx=5,pady=5)



cancel = customtkinter.CTkButton(displayframe, text="Cancel",text_color="red",command=cancel)

cancel.grid(row=2,column=1)





root.mainloop()

