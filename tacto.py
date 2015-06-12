#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta

global numtouch
global touch
global tiempo

numtouch=0
touch = False
tiempo = datetime.now()

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
                    print "dos toques"
                    numtouch=0
            else:
                numtouch=0
                touch = False
        print numtouch


"""    try:
        rospy.wait_for_message(touch, TOUCH_MSG, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Topico: " + TOUCH_MSG + " NO FUNCIONA.\nEXCEPCION DE TOPICO: " + str(e))
        return
    touch_msg = rospy.ServiceProxy(SERVOS_SRV, MoveServo)
"""

