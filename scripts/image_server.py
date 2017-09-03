#!/usr/bin/env python

from objectattention_ros.srv import *
import rospy
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

bridge = CvBridge()
def handle_kinect_images(req):
    return KinectImageResponse(img)

def kinect_image_callback(data):
    global img
    img = data
    img = bridge.imgmsg_to_cv2(img, "bgr8")
    img = img.flatten()

def gravity_torques_server():
    rospy.init_node('kinect_image')
    s = rospy.Service('kinect_image', KinectImage, handle_kinect_images)
    rospy.Subscriber("/kinect2/qhd/image_color", Image, kinect_image_callback)
    rospy.spin()

if __name__ == "__main__":
    gravity_torques_server()