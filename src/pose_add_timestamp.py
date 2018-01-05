#! /usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped, Quaternion
from turtlesim.msg import Pose
from tf.transformations import quaternion_from_euler


class PoseStampAdder:
    def __init__(self):
        self._Pose_sub = rospy.Subscriber("/turtle1/pose", Pose, self.callback)
        self._Pose_stamped_pub = rospy.Publisher("/turtle1/pose_stamped", PoseStamped, queue_size=10)

    def callback(self, Pose_in):
        Pose_stamped = PoseStamped()
        Pose_stamped.header.stamp = rospy.Time.now()

        Pose_stamped.pose.position.x = Pose_in.x
        Pose_stamped.pose.position.y = Pose_in.y

        ori = quaternion_from_euler(0, 0, Pose_in.theta)
        Pose_stamped.pose.orientation = Quaternion(ori[0], ori[1], ori[2], ori[3])

        self._Pose_stamped_pub.publish(Pose_stamped)


if __name__ == "__main__":
    rospy.init_node("PoseStampAdder", anonymous=True)
    tsa = PoseStampAdder()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
