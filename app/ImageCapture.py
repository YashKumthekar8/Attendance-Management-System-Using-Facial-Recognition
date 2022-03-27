import cv2
from cv2 import *
import os


def CaptureImage(name):
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        path=os.getcwd()
        path=os.path.join(path,"media")
        path=os.path.join(path,"unknown")
        path=os.path.join(path,f"{name}.jpg")
        cv2.imshow(name, image)
        cv2.imwrite(path, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No image detected. Please! try again")
