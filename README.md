# Car Plate Recognition System for Oman
Managing and administering the transportation system has become more difficult as the number of vehicle ownership is increasing day by day. Due to that there must be a system that can help in controlling vehicle access at factorial/industrial areas, parking/traffic management and as well as in law enforcement.
 
This project is using deep learning and computer vision techniques, with developing a desktop application that enables users to detect the Omani car plate by using object detection model YOLO (You only look once) which scans an image, identifies and classifies the car plate region. In addition, this system will extract the number and letters from the detected car plate by using Tesseract, an OCR (Optical character recognition) engine. It is considered a good OCR due to the quality of it, particularly in challenging situations like reading extremely small text.
 
The project is based on a dataset of 900 labeled images. Training data is conducted over 30 epochs, from which the obtained mAP@.5 is approximately 92%, indicating that the model has learned the task almost perfectly. For evaluating OCR results, Levenshtein distance is used to compare between original text and OCR resulted text. With applying some preprocessing to enhance the image the accuracy was approved to 65.646%.

# Installation
To run this project locally, follow these steps:

1) Clone this repository to your local machine using git clone https://github.com/Shifa-Alrashdi/Car_Plate_Recognition.git
2) Install the necessary dependencies (e.g., open-source OCR libraries)
3) Open Desktop_App and run it.

# Desktop App Demo
![1685523502435](https://github.com/Shifa-Alrashdi/Running_Game/assets/128242451/ece64469-1b49-4058-afb3-cb3fa715da38)
![1685523503374](https://github.com/Shifa-Alrashdi/Running_Game/assets/128242451/77827413-8d60-49ba-9ebf-5d874a2e0524)

# Poster 
![image](https://github.com/Shifa-Alrashdi/Running_Game/assets/128242451/4289f6e9-d14e-43a9-a090-290e937146f6)
