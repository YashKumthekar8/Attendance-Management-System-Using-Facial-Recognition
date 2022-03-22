from base64 import encode
from tkinter import image_names
from cv2 import COLOR_RGB2BGR
import face_recognition
import os
import cv2
from faceRego2 import *

#Function for adding the location of faces that are  missed
def IncreasingAccuracy(location,imgPath):
  addLocation=DlibDetection(imgPath)
  #addLocation1=HarCasacadeClassifierDetection(imgPath)

  for i in addLocation:
      location.append(i)

    
  print(len(location))
  return location    



#Directory for known and unknown faces
known_faces_dir="known"
unknown_faces_dir="unknown"


#Setting the value of tolerance,frame_thickness and font_size  
tolerance=0.5
frame_thickness=7
font_size=10

#Specifying the model
model="hog"

#Loading the known faces from the known faces directory
known_faces=[]

#Here person name is the image name
known_name=[]

#Loading the Registered(Known faces)
for name in os.listdir(known_faces_dir):
    image=face_recognition.load_image_file(f"{known_faces_dir}/{name}")
    encoding=face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_name.append(name)


#Loading the unknown faces
for name in os.listdir(unknown_faces_dir):
    image=face_recognition.load_image_file(f"{unknown_faces_dir}/{name}")

    #Co-ordinate of all the faces in the image
    locations=face_recognition.face_locations(image,model=model)
     
    #Passing the location to fucntion for adding the missing faces 
    #locations=IncreasingAccuracy(locations,f"{unknown_faces_dir}/{name}")

    #Here we are doing an encoding on the loaction of the faces 
    encoding=face_recognition.face_encodings(image,locations)

    #code for drawing the rectangle and writing the name
    image=cv2.cvtColor(image,COLOR_RGB2BGR)

    match=None
    #Looping over each face detected and finding the known face match for it
    for face,location in zip(encoding,locations):
        #Here result is an list of boolean whether that particular gace os present or not
        # top_left=(location[3],location[0])
        # bottom_right=(location[1],location[2])
        # color=[0,255,0]
        # cv2.rectangle(image,top_left,bottom_right,color,frame_thickness)
            
        results=face_recognition.compare_faces(known_faces,face,tolerance)

     
        if True in results:
            match=known_name[results.index(True)]
            print(match)
            #For plotting the rectangle and writing the name
            top_left=(location[3],location[0])
            bottom_right=(location[1],location[2])
            color=[0,255,0]
            cv2.rectangle(image,top_left,bottom_right,color,frame_thickness)
            
            #For Righting the name on the image
            top_left=(location[3],location[2])
            bottom_right=(location[1],location[2]+22)
            cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)
            cv2.putText(image,match,(location[3]+10,location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,3.5,font_size) 
    
    image=cv2.resize(image,(500,500))
    cv2.imshow(name,image)
    cv2.waitKey(0)    


