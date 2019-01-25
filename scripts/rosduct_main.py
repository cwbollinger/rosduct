#!/usr/bin/env python

import rospy
from rosduct.rosduct_impl import ROSduct

if __name__ == '__main__':
    rospy.init_node('rosduct')
    r = ROSduct()
    try:
        r.spin()
    except rospy.ROSInterruptException:
        rospy.logwarn('ROS Shutting down...')
