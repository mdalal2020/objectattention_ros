#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node('VideoPublisher', anonymous=True)

VideoRaw = rospy.Publisher('VideoRaw', Image, queue_size=10)

cam = cv2.VideoCapture()

bridge = CvBridge()

while True:
    meta, frame = cam.read()
    # import ipdb; ipdb.set_trace()
    # msg_frame = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
    #
    # VideoRaw.publish(msg_frame, "RGB8")
    cv2.imshow('Windows', frame)

    time.sleep(0.1)