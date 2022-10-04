#!/usr/bin/env python #Used to tell ROS what language you are useing
import rospy
from std_msgs.msg import Float64 #telling ros waht message format to use, Float 64 is used great for non interger values

#creating node "cylinder_input"
rospy.init_node("cylinder_input")
#creating a rospy object that is a publisher
#its going to publish to the the /radius object
#its message type is Float64
#queue_size = 10(dont worry abouyt it)
radius_pub = rospy.Publisher("/radius",Float64, queue_size=10)
height_pub = rospy.Publisher("/height",Float64, queue_size=10)
density_pub = rospy.Publisher("/density",Float64, queue_size=10)

radius = float(input("Enter radius: "))
height = float(input("Enter heaight: "))
density = float(input("Enter density: "))

#continue to run this code while rospy is running
while not rospy.is_shutdown():
	radius_pub.publish(radius)
	height_pub.publish(height)
	density_pub.publish(density)
	#This will prevent this from clogging the network
	rospy.sleep(0.1)
