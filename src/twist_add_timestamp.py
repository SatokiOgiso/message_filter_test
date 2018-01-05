#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, TwistStamped


class TwistStampAdder:
    def __init__(self):
        self._twist_sub = rospy.Subscriber("/turtle1/cmd_vel", Twist, self.callback)
        self._twist_stamped_pub = rospy.Publisher("/turtle1/cmd_vel_stamped", TwistStamped, queue_size=10)

    def callback(self, twist_in):
        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = rospy.Time.now()
        twist_stamped.twist = twist_in
        self._twist_stamped_pub.publish(twist_stamped)


if __name__ == "__main__":
    tsa = TwistStampAdder()
    rospy.init_node("TwistStampAdder", anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
