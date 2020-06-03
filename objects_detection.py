import jetson.inference                                   # NVIDIA module for object detection
import jetson.utils                                       # NVIDIA module for camera capture
import sys						  # to call functions

net= jetson.inference.detectNet("SSD-Mobilenet-v2", threshold=0.5)         # load the object detection model

camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")                  # for camera capture

display = jetson.utils.glDisplay()                                         # create display with glDisplay object

count=0
while display.IsOpen():
	
	img, width, height = camera.CaptureRGBA()                          # camera capture returning with width 
	
	detections = net.Detect(img, width, height)                        # perform detections, this takes img, width and height from camera.capture() 
	if detections:
		print("detected {:d} objects :".format(len(detections)))   # print the detections 
		count= count+1
		for detection in detections:
			print(detection)                                   # print Object Detection Result like classID
	display.RenderOnce(img, width, height)                             # render the image

	display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))  # window title anf Fps	  	

print("Total number of objects detected:"),	
print(count)

