#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


#work done when subscriber is given data
#data is the message comming accross
def callback(data):
	radius = data.data #pull data into radius
	squared_radius = radius * radius
	rospy.loginfo("radius: %f, squared_radius: %f", radius, squared_radius)
	pub.publish(squared_radius)

rospy.init_node("radius_squarer")#intialize node
pub = rospy.Publisher("/radius_squared",Float64, queue_size = 10)#create publisher
rospy.Subscriber("/radius", Float64, callback)#subscriber "radius" when a mssage is passed it automatically calls the callback function. each subscriper has to have a callback function 
rospy.spin() #keeps program alive in ros, replaces while loop

