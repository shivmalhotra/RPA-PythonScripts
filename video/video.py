from SimpleCV import *
import time

c = Kinect()
vs = VideoStream("out.avi")

framecount = 0
while(framecount < 100):
    c.getImage().save(vs)
    time.sleep(0.1)
    framecount+= 1