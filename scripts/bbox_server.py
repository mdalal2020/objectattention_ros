#!/usr/bin/env python

from objectattention_ros.srv import *
import rospy
import numpy as np
from  std_msgs.msg import Float64MultiArray

def handle_bbox(req):
    return BBoxResponse(bbox)

def bbox_callback(data):
    global bbox
    bbox = data.data

def gravity_torques_server():
    rospy.init_node('bbox')
    s = rospy.Service('bbox_server', BBox, handle_bbox)
    rospy.Subscriber("/objectattention/bbox", Float64MultiArray, bbox_callback)
    rospy.spin()

if __name__ == "__main__":
    gravity_torques_server()