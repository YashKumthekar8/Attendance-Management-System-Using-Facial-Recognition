from base64 import encode
from pydoc import locate
from tkinter import image_names
from cv2 import COLOR_RGB2BGR
import face_recognition
import os
import cv2
from .face_recognition import *
import datetime
from dateutil.relativedelta import relativedelta
	


def faces_name(temp,known_name,results):
    for ans in results:
        k=0
        for j in ans:
            if j:
                temp.append(known_name[k])
            k+=1
    return temp



#Function which returns the list of faces recognised from the current Image
def Recognize(ImgPath):
    known_faces_dir="media/images"
    tolerance=0.5

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


    #Dictionary Containing the inage and faces present


    #Loading the unknown faces
    
    temp=[]    
    #Loading the Image
    image=face_recognition.load_image_file(ImgPath)
        
    #Using the FaceRecognition Module
    location=FaceRegonitionModule(ImgPath)
    encoding=face_recognition.face_encodings(image,location)
    ans=[]   
    for face,location in zip(encoding,location):
        results=face_recognition.compare_faces(known_faces,face,tolerance)
        ans.append(results)
    temp=faces_name(temp,known_name,ans)     

    #Using the Dlib Detection
    ans=[]
    location=DlibDetection(ImgPath)
    encoding=face_recognition.face_encodings(image,location)   
    for face,location in zip(encoding,location):
        results=face_recognition.compare_faces(known_faces,face,tolerance)
        ans.append(results)
    temp=faces_name(temp,known_name,ans)     
    
    #Using the Har Casacde Detection
    ans=[]
    location=HarCasacadeClassifierDetection(ImgPath)
    encoding=face_recognition.face_encodings(image,location)   
    for face,location in zip(encoding,location):
        results=face_recognition.compare_faces(known_faces,face,tolerance)
        ans.append(results)
    temp=faces_name(temp,known_name,ans)     

    return set(temp)
        

        

#Function for convertong the weekno to corresponding week dates
def weekNoToDates(year,weekno):
	dates=[]
	date = datetime.date(year, 1, 1) + relativedelta(weeks=+weekno)
	dates.append(date)
	i=-1
	while i!=-7:
		dates.append(date+datetime.timedelta(days=i))
		i=i-1

	dates.reverse()
	return dates	
