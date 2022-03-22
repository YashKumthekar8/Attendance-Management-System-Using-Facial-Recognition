from unittest import result
import dlib
import cv2
import matplotlib.pyplot as plt
from imutils import face_utils
from base64 import encode
from tkinter import image_names
from cv2 import COLOR_RGB2BGR
import face_recognition
import os




#Detection Using Dlib
def DlibDetection(imgPath):
    image=cv2.imread(imgPath)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face_detect=dlib.get_frontal_face_detector()
    result=face_detect(gray,1)

    loc_set=[]
    for (i,rect) in enumerate(result):
        (x,y,w,h)=face_utils.rect_to_bb(rect)
        loc_set.append((x,y,w,h))

    return loc_set        


#Detection Using HarCascadeClassifier
def HarCasacadeClassifierDetection(imgPath):
    #GETTING THE FACECASCADDE CLASSIFIER
    facecascade=cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

    img=cv2.imread(imgPath)

    #FIRST CONVERT THE IMAGE TO GREY SCALE
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #DETECTING THE FACE
    faces=facecascade.detectMultiScale(img_gray,1.1,4)
    face_loc=[] 
    for i in faces:
        temp=(i[0],i[1],i[2],i[3])
        face_loc.append(temp)

    return face_loc    
    


def FaceRegonitionModule(imgPath):
        model="hog"
        image=face_recognition.load_image_file(imgPath)

        #Co-ordinate of all the faces in the image
        locations=face_recognition.face_locations(image,model=model)
        
        return locations

        