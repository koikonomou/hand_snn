import time
import math
import rospy
import numpy as np
from std_msgs.msg import Float64


class Position(object):

    def __init__(self):
        rospy.init_node('new_gripper_init_pose', anonymous = True)
        self.rate = rospy.get_param("rate", 10)

        self.ffj0 = rospy.get_param("joint_ffj0", 1.50)
        self.ffj3 = rospy.get_param("joint_ffj3", 0.0)
        self.ffj4 = rospy.get_param("joint_ffj4", 0.0)

        self.lfj0 = rospy.get_param("joint_lfj0", 1.5)
        self.lfj3 = rospy.get_param("joint_lfj3", 0.30)
        self.lfj4 = rospy.get_param("joint_lfj4", 0.0)
        self.lfj5 = rospy.get_param("joint_lfj5", 0.70)

        self.mfj0 = rospy.get_param("joint_mfj0", 0.20)
        self.mfj3 = rospy.get_param("joint_mfj3", 0.30)
        self.mfj4 = rospy.get_param("joint_mfj4", 0.0)

        self.rfj0 = rospy.get_param("joint_rfj0", 0.20)
        self.rfj3 = rospy.get_param("joint_rfj3", 0.30)
        self.rfj4 = rospy.get_param("joint_rfj4", 0.0)

        self.thj1 = rospy.get_param("joint_thj1", 0.65)
        self.thj2 = rospy.get_param("joint_thj2", 0.50)
        self.thj3 = rospy.get_param("joint_thj3", 0.30)
        self.thj4 = rospy.get_param("joint_thj4", 0.40)
        self.thj5 = rospy.get_param("joint_thj5", 0.20)

        self.wrj1 = rospy.get_param("joint_wrj1", -0.10)
        self.wrj2 = rospy.get_param("joint_wrj2", 0.0)

        # Forefinger
        self.pub_ffj0 = rospy.Publisher('/sh_rh_ffj0_position_controller/command', Float64, queue_size=10)
        self.pub_ffj3 = rospy.Publisher('/sh_rh_ffj3_position_controller/command', Float64, queue_size=10)
        self.pub_ffj4 = rospy.Publisher('/sh_rh_ffj4_position_controller/command', Float64, queue_size=10)
        # Little finger
        self.pub_lfj0 = rospy.Publisher('/sh_rh_lfj0_position_controller/command', Float64, queue_size=10)
        self.pub_lfj3 = rospy.Publisher('/sh_rh_lfj3_position_controller/command', Float64, queue_size=10)
        self.pub_lfj4 = rospy.Publisher('/sh_rh_lfj4_position_controller/command', Float64, queue_size=10)
        self.pub_lfj5 = rospy.Publisher('/sh_rh_lfj5_position_controller/command', Float64, queue_size=10)
        # Middle finger
        self.pub_mfj0 = rospy.Publisher('/sh_rh_mfj0_position_controller/command', Float64, queue_size=10)
        self.pub_mfj3 = rospy.Publisher('/sh_rh_mfj3_position_controller/command', Float64, queue_size=10)
        self.pub_mfj4 = rospy.Publisher('/sh_rh_mfj4_position_controller/command', Float64, queue_size=10)
        # Ring finger
        self.pub_rfj0 = rospy.Publisher('/sh_rh_rfj0_position_controller/command', Float64, queue_size=10)
        self.pub_rfj3 = rospy.Publisher('/sh_rh_rfj3_position_controller/command', Float64, queue_size=10)
        self.pub_rfj4 = rospy.Publisher('/sh_rh_rfj4_position_controller/command', Float64, queue_size=10)
        # Thumb
        self.pub_thj1 = rospy.Publisher('/sh_rh_thj1_position_controller/command', Float64, queue_size=10)
        self.pub_thj2 = rospy.Publisher('/sh_rh_thj2_position_controller/command', Float64, queue_size=10)
        self.pub_thj3 = rospy.Publisher('/sh_rh_thj3_position_controller/command', Float64, queue_size=10)
        self.pub_thj4 = rospy.Publisher('/sh_rh_thj4_position_controller/command', Float64, queue_size=10)
        self.pub_thj5 = rospy.Publisher('/sh_rh_thj5_position_controller/command', Float64, queue_size=10)
        # Wrist
        self.pub_wrj1 = rospy.Publisher('/sh_rh_wrj1_position_controller/command', Float64, queue_size=10)
        self.pub_wrj2 = rospy.Publisher('/sh_rh_wrj2_position_controller/command', Float64, queue_size=10)



    def spin(self):
        rate = rospy.Rate(self.rate)

        while not rospy.is_shutdown():
            rate.sleep()
            msg_ffj0 = Float64()
            msg_ffj3 = Float64()
            msg_ffj4 = Float64()

            msg_lfj0 = Float64()
            msg_lfj3 = Float64()
            msg_lfj4 = Float64()
            msg_lfj5 = Float64()

            msg_mfj0 = Float64()
            msg_mfj3 = Float64()
            msg_mfj4 = Float64()

            msg_rfj0 = Float64()
            msg_rfj3 = Float64()
            msg_rfj4 = Float64()

            msg_thj1 = Float64()
            msg_thj2 = Float64()
            msg_thj3 = Float64()
            msg_thj4 = Float64()
            msg_thj5 = Float64()

            msg_wrj1 = Float64()
            msg_wrj2 = Float64()
###### Robot arm full position (a1= 0, a2=-90, a3= 0, a4= 0, a5= 0 , a6= 0) ######
###### Robot initial position (a1= 0, a2=-95, a3= 50, a4= 0, a5= 100 , a6= 0) ######
##pose 0, -0.87, 1.74, 0, 0.61, 0
###### Robot joint limits in rads (a1= , a2= , a3= , a4= ,a5= 2.09, a6=  ) ######

            msg_ffj0.data = self.ffj0
            msg_ffj3.data = self.ffj3
            msg_ffj4.data = self.ffj4

            msg_lfj0.data = self.lfj0
            msg_lfj3.data = self.lfj3
            msg_lfj4.data = self.lfj4
            msg_lfj5.data = self.lfj5

            msg_mfj0.data = self.mfj0
            msg_mfj3.data = self.mfj3
            msg_mfj4.data = self.mfj4

            msg_rfj0.data = self.rfj0
            msg_rfj3.data = self.rfj3
            msg_rfj4.data = self.rfj4

            msg_thj1.data = self.thj1
            msg_thj2.data = self.thj2
            msg_thj3.data = self.thj3
            msg_thj4.data = self.thj4
            msg_thj5.data = self.thj5

            msg_wrj1.data = self.wrj1
            msg_wrj2.data = self.wrj2

            self.pub_ffj0.publish(msg_ffj0)
            self.pub_ffj3.publish(msg_ffj3)
            self.pub_ffj4.publish(msg_ffj4)
            # Little finger
            self.pub_lfj0.publish(msg_lfj0)
            self.pub_lfj3.publish(msg_lfj3)
            self.pub_lfj4.publish(msg_lfj4)
            self.pub_lfj5.publish(msg_lfj5)
            # Middle finger
            self.pub_mfj0.publish(msg_mfj0)
            self.pub_mfj3.publish(msg_mfj3)
            self.pub_mfj4.publish(msg_mfj4)
            # Ring finger
            self.pub_rfj0.publish(msg_rfj0)
            self.pub_rfj3.publish(msg_rfj3)
            self.pub_rfj4.publish(msg_rfj4)
            # Thumb
            self.pub_thj1.publish(msg_thj1)
            self.pub_thj2.publish(msg_thj2)
            self.pub_thj3.publish(msg_thj3)
            self.pub_thj4.publish(msg_thj4)
            self.pub_thj5.publish(msg_thj5)
            # Wrist
            self.pub_wrj1.publish(msg_wrj1)
            self.pub_wrj2.publish(msg_wrj2)



if __name__ == "__main__" :
    node = Position()
    node.spin()