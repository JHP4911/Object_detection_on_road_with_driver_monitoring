# Self Driving Car - Perception Drive

• Based on NVIDIA Jetson Nano, TensorRT, OpenCV, Python 

• Real-Time Traffic detection.  

• Driver face, eye and smile detection. 

• Driver drowsiness detection.

• Driver not looking straight detection. 

• Created GUI for showing failures, number and type of objects detected 
  on road. 

## Files inside this Repository
1 - objects_detection.py
> Detects objects on a live camera feed. It uses  SSD-Mobilenet-v2 model for 91-class detection.based on TensorRT on NVIDIA Jetson Nano. [Coding Your Own Object Detection Program](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-example-2.md)

2 - GUI_output.py
> It shows the failures, number and type of objects detected during the drive on a Graphical user interface.

3 - face_eyes_smile_detection.py
> Detection of face, eyes and smile of a driver using OpenCV, Haarcascade classifiers.

4 - eye_monitoring.py
> Detects and monitor eyes and  alerts with sound when driver is sleepy or drowsy. It also alert when driver don't look straight.
