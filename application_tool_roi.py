# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:55:27 2019

This code will store the area that user crops from display window to config.json file.
In the fromat of dictionary={"cameraname":(x,y,w,h).}
@author: soumya.doddagoudar
"""

import numpy as np
import cv2
import json
import os



def main():
   
    #define dictionary to read config file contents
    config_dict={}
    
    #reading config file
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            try:
                config_dict = json.load(f)
            except:
                print("config value is empty")
        
    input_video_path=str(input("Enter video path without quotes\n"))
  
    camera_name=str(input("enter camera name: allen,or,limerick,or,rosemon\n"))
    #define window for display
    cv2.namedWindow("draw_rectangle",cv2.WINDOW_NORMAL)
    #read image
    camera = cv2.VideoCapture(input_video_path)
    ok, image=camera.read()
   
    #select rectangle region to be cropped
    bbox1 = cv2.selectROI('draw_rectangle', image)
    print(bbox1)
    #assign or store new value to config_dict
    config_dict[camera_name]=bbox1
    #store or write new value to config.json file          
    with open('config.json', 'w') as f:
        json.dump(config_dict, f)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #exit()
        
    #cv2.waitKey(1)
    #release camera and destroy display windows
    camera.release()
    cv2.destroyAllWindows()
    #exit()
    
main()
