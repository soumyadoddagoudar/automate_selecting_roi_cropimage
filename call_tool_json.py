# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:28:59 2019

This code will read values from config.json file and passes only that area of image to process further.
config.json file has contents {"qu": [73, 216, 1370, 721]}, where "qu" is the camera name(any string/value),and followed by list(x,y,w,h)
@author: soumya.doddagoudar
"""

import cv2
import sys
import json
def main():
    
    
    input_video_path=str(input("Enter video path without quotes\n"))
    
    camera_name=str(input("enter camera name: \n"))
    
    #read already stored values from config.json file to dictionary
    config_dict={}
    
    with open('config.json', 'r') as f:
        try:
                config_dict = json.load(f)
        except:
                print("config value is empty")
        
    #read input video    
    camera = cv2.VideoCapture(input_video_path)
    #read image
    ok, image=camera.read()
    #extract values of cropped region from dictionary
    (x,y,w,h)=config_dict[camera_name]
    ymin=y
    ymax=y+h
    xmin=x
    xmax=x+w
    cropped = image[ymin:ymax, xmin:xmax]
    #cv2.imwrite("croppedimg.jpg",cropped)
    #initialize and display window
    cv2.namedWindow("cropped Feed",cv2.WINDOW_NORMAL)
    cv2.imshow("cropped Feed", cropped)
    cv2.waitKey(5000) 
    #destroy and release windows.
    camera.release()
    cv2.destroyAllWindows()
#    key = cv2.waitKey(1) & 0xFF
#    if key == ord("q"):
#        camera.release()
#        cv2.destroyAllWindows() 
#        exit()

    
    
    
main()
