#!/usr/bin/env python3
#license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from math import radians

def square_movement_node():
    pub = rospy. Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('tbsim_driver', anonymous=True)
    rate = rospy.Rate(1)
    
    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 0
    
    turn_cmd = Twist()
    turn_cmd.linear.x = 0
    turn_cmd.angular.z = radians(90)

while not rospy.is_shutdown():
    rate.sleep()
    pub.publish(move_cmd)
    rate.sleep()
    
    pub.publish(turn_cmd)
    rate.sleep()

if name == '___main___':
    try:
        square_movement_node()
    except rospy.ROSInterruptException:
        pass
