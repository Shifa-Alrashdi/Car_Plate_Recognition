import tkinter



import tkinter.messagebox



import customtkinter



from tkVideoPlayer import TkinterVideo



from tkinter.filedialog import askopenfile



from detect8 import detect 



from PIL import Image, ImageTk



import os

from tkinter.ttk import *
 
import cv2


from time import sleep
from tkinter import Tk, Label
from sys import exit

class LoadingSplash:
    def __init__(self,root2):
        self.root2 = root2
        
        #loading text
        Label(self.root2, text="Loading...", font="Bahnschrif 15",
              bg='black', fg='blue').place(x=490, y=320)
              
             
        #loading blocks
        for i in range(16):
            Label(self.root2, bg="blue", width=2, height=1).place(x=(i+22)*22, y=350)
        
        self.root2.update()
        self.play_animation()
        #self.detect3()
        #self.root2.mainloop()
        
    def play_animation(self):
        for i in range(50):
            for j in range(16):
                Label(self.root2, bg="blue", width=2, height=1).place(x=(j+22)*22, y=350)
                sleep(0.06)
                self.root2.update_idletasks()
                
                Label(self.root2, bg="#1F2732", width=2, height=1).place(x=(j+22)*22, y=350)
        else:
            
            exit(0)
            
    
        
            
class vidoFrame():

    def __init__(self, window, cap):

        self.window = window

        self.cap = cap

        #self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        #self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

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

imgFile= None
filename = None

def uploadImage():


    global imgFile
    print("uploadImage click")



    global img



    f_types = [('Jpg Files', '*.jpg')]



    imgFile = askopenfile(filetypes=f_types)

    

   

    

    if imgFile is not None:

        #opne 

        imgOpne = Image.open(imgFile.name)

        #resize 

        imgResized = imgOpne.resize((700,650), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(imgResized)
        
        

        #put it in label 

        imageLable = tkinter.Label(inputFrame,image=img) 



        imageLable.grid(row=0,column=1)

        

        #Detection
        
        
          




def uploadVideo():



    print("uploadVideo click")



    file = askopenfile( filetypes=[('Video Files',['*.mp4',"*.mov",'*.jpg'])])



    if file is not None:



        global filename



        filename = file.name


        vidoFrame(inputFrame, cv2.VideoCapture(filename))
        





        '''

        VD = detect(filename)



        if VD is not None:



            videoplayer = TkinterVideo(master=inputFrame, scaled=True)



            videoplayer.load(r"{}".format(VD) )



            videoplayer.pack()



            videoplayer.grid(row=1,column=1,padx=5,pady=5)



            videoplayer.play()
            '''
        


def cancel():

    global imgFile
    global filename
    imgFile= None
    filename = None
    
    for widgets in inputFrame.winfo_children():



      widgets.destroy()
      
def detectt():
    
    #print(inputFrame.)
    
    for widgets in inputFrame.winfo_children():
      widgets.destroy()
    global imgFile    
    
    
    if imgFile is not None:
        #inputFrame.destroy()
        ID = None
        if ID is None:
            
            
            ID = detect(imgFile.name) 
            LoadingSplash(inputFrame)
            
    
            imgOpne2 = Image.open(ID)
      
            imgResized2 = imgOpne2.resize((700,650), Image.ANTIALIAS)
      
            img2 = ImageTk.PhotoImage(imgResized2)
      
           
      
            imageLable2 = tkinter.Label(inputFrame,image=img2) 
      
            imageLable2.image = img2
            imageLable2.grid(row=1,column=1)
    
            global filename
            
            if filename is not None:
                
                VD = detect(filename)
            
                if VD is not None:
            
                    vidoFrame(inputFrame, cv2.VideoCapture(VD))
        
      
    
      
    




    


    '''
    for widgets in outputFrame.winfo_children():



      widgets.destroy()

    '''





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

inputFrame = customtkinter.CTkFrame(displayframe,width=750,height=500)



inputFrame.grid(row=0,padx=5,pady=5,columnspan=2)


#outputFrame = customtkinter.CTkFrame(displayframe,width=750,height=260)



#outputFrame.grid(row=1,column=1,padx=5,pady=5)

cancel = customtkinter.CTkButton(displayframe, text="Cancel",text_color="white",command=cancel)

cancel.grid(row=2,column=1)

detect2 = customtkinter.CTkButton(displayframe, text="Detect",text_color="white",command=detectt)

detect2.grid(row=2,column=0)
#Span(mapping=detect2, *, ignore_unknown_fields=False, **kwargs)



root.mainloop()



