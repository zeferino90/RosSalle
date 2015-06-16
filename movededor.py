#!/usr/bin/env python

import rospy
from scripts.move_robot import move_head
from sounds import *
from airos4_msgs.msg import Touch
from std_msgs.msg import UInt32MultiArray
from heart import *
from mouth import *
from datetime import datetime
from datetime import timedelta
import time

global numtouch
global touch
global tiempo
global eyelid
global count

numtouch=0
touch = False
tiempo = datetime.now()
eyelid = True
count = 0


def quejate():
    global eyelid
    head_center = 0.4
    print "Eyelid {}".format(eyelid)
    move_head(0, eyelid, 1) #head, eyelid, eyebrow
    time.sleep(0.5)
    move_head(1, eyelid, 1)
    time.sleep(0.5)
    move_head(head_center, eyelid, 1)
    time.sleep(0.5)
    eyelid = not eyelid
    print "Eyelid2 {}".format(eyelid)
    move_head(head_center, eyelid, 0)

    set_heart_color(255,0, 0)
    play_audio("human-babycry")
    time.sleep(3)
    set_heart_color(255, 255, 255)
    eyelid = not eyelid
    move_head(eyebrow=1, eyelid= eyelid)




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

    elif data.left == True and data.right == True:
        print "dos touch"
        play_audio_file("/home/pi/grrr.mp3")
        set_heart_color(0, 255, 255)
        move_head(eyelid=0)
        time.sleep(4)
        set_heart_color(255, 255, 255)
        move_head(eyelid=1)



def customMarker(data):
    global count
    try:
        if len(data.data) > 0:
            count = count + 1
            if count == 5:
                say(str(data.data[0]))
                count = 0
        mouth_print("(_________)")
    except rospy.ROSException as e:
        rospy.logerr("Service: " + SRV_PLAY + " does not appear to be running.\nReal exception msg: " + str(e))
        return




rospy.init_node('servos')
#move_head(head_pan=4.0,eyelid=0.0,eyebrow=0.0)
pubtouch = rospy.Subscriber('/airos4/touch/touch', Touch, touch_rd)
pubMarker = rospy.Subscriber('/aruco/markers_list', UInt32MultiArray, customMarker)
rospy.spin()

 
