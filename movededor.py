#!/usr/bin/env python

import rospy
from scripts.move_robot import move_head
from airos4_msgs.msg import Touch
from std_msgs.msg import String	
from tacto import *
from datetime import datetime
from datetime import timedelta
import time

global numtouch
global touch
global tiempo

numtouch=0
touch = False
tiempo = datetime.now()

def quejate():
    move_head(0, 1, 1) #mirar valores para mover cabeza a un lado y luego al otro
    time.sleep(0.5)
    move_head(1, 1, 1)


def touch_rd(data):
    global numtouch
    global touch
    global tiempo
#	print data
    if data.head==True:
        numtouch+=1
        if not touch:
            tiempo =datetime.now()
            touch = True
        if touch:
            tnew = datetime.now()
            if tnew - tiempo < timedelta(seconds=2):
                if numtouch==3:
                    quejate()
                    numtouch=0
            else:
                numtouch=0
                touch = False
        print numtouch



rospy.init_node('servos')
#move_head(head_pan=4.0,eyelid=0.0,eyebrow=0.0)
pubtouch = rospy.Subscriber('/airos4/touch/touch', Touch, touch_rd)
rospy.spin()

 
