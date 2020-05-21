import jetson.inference
import jetson.utils
import sys

net= jetson.inference.detectNet("SSD-Mobilenet-v2", threshold=0.5)

camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")  # using V4L2

display = jetson.utils.glDisplay()

count=0
while display.IsOpen():
	
	img, width, height = camera.CaptureRGBA()
	
	detections = net.Detect(img, width, height)
	if detections:
		print("detected {:d} objects :".format(len(detections)))
		count= count+1
		for detection in detections:
			print(detection)
	display.RenderOnce(img, width, height)

	display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))	  	

print("Total number of objects detected:"),	
print(count)

