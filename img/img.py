from SimpleCV import *

c = Kinect()

x = 0
while(x < 10):
    c.getImage().save("Image"+str(x)+".png")
    x+= 1