#!/usr/bin/env python

import rospy
from move_robot import move_head

if __name__ == '__main__':
    rospy.init_node('ttrefdagdg')
    move_head(head_pan=0.5, eyelid=1.0, eyebrow=1.0) # center head, eyelid up, eyebrow up

