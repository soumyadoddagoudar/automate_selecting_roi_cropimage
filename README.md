# Automate_selecting_roi_cropimage
To automate selection of ROI and use only that part of image/video to process.

## Requirements

•	opencv 3.4.2

•	spyder/anaconda prompt

•	json

## Usage

open spyder or anaconda prompt and type below command:

•	python application_tool_roi.py
  
It will ask for input video path, and camera_name(any string) provide these values. display window will be poped up select rectangle region/area of interest on image by using mouse and hit enter. It will save the values of selected region(x,y,w,h) to config.json file.
  
•	python call_tool_json.py

After executing application_tool_roi.py, run above code and provide video path and camera_name(one which you gave before). This will take(x,y,w,h) values stored in config.json file corresponding to camera_name you specify and display only that part of image.

## Example

![alt text]( https://github.com/soumyadoddagoudar/automate_selecting_roi_cropimage/blob/master/data/airport_2.png)



  
  


