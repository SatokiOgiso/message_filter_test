#!/usr/bin/env python

import rospy
import message_filters
from geometry_msgs.msg import TwistStamped, PoseStamped


def callback(msg1, msg2):
    rospy.loginfo(msg1)
    rospy.loginfo(msg2)


def main():
    rospy.init_node("time_sync", anonymous=True)
    cmd_sub = message_filters.Subscriber('/turtle1/cmd_vel_stamped', TwistStamped)
    pose_sub = message_filters.Subscriber('/turtle1/pose_stamped', PoseStamped)

    ts = message_filters.ApproximateTimeSynchronizer([cmd_sub, pose_sub], 10, 0.1)
    ts.registerCallback(callback)
    rospy.spin()


if __name__ == '__main__':
    main()