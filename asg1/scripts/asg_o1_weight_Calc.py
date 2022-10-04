#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from asg1.msg import Cylinder


Density = 0
Volume = 0

Denisty_found = False
Volume_found = False

#callback functions
def weight_callback(data):
	global Density
	global Denisty_found
	Density = data.data
	Denisty_found = True

def cylinder_callback(data):
	global Volume
	global Volume_found
	Volume = data.volume
	Volume_found = True

#calculate weight
def weight_calc():
	if Volume_found and Denisty_found:
		weight = Volume * Density
		weight_pub.publish(weight)



rospy.init_node("weight_calc")#intialize node
weight_pub = rospy.Publisher("/weight",Float64, queue_size = 10)#create publisher
rospy.Subscriber("/density", Float64, weight_callback)
rospy.Subscriber("/cylinder", Cylinder, cylinder_callback)


while not rospy.is_shutdown():
	weight_calc()
	rospy.sleep(0.1)
