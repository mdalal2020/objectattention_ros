#!/usr/bin/env python
import rospy
import cv2
from  std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def image_publisher():
    cap = cv2.VideoCapture(0)
    pub = rospy.Publisher('image_publisher', Image, queue_size=10)
    rospy.init_node('image_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        # frame = frame.flatten()
        # new_msg = Float64MultiArray()
        # new_msg.data = frame
        # pub.publish(new_msg)
        frame = bridge.cv2_to_imgmsg(frame, encoding="rgb8")
        pub.publish(frame)
        rate.sleep()

if __name__ == '__main__':
    try:
        image_publisher()
    except rospy.ROSInterruptException:
        pass
