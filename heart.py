__author__ = 'zeferino'

import rospy
from airos4_msgs.srv import SetColor, SetColorRequest


HEART_SRV = "/airos4/heart/set_color"


def set_heart_color(red, green, blue):
    try:
        rospy.wait_for_service(HEART_SRV, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Service: " + HEART_SRV + " does not appear to be running.\nReal exception msg: " + str(e))
        return
    heart_srv = rospy.ServiceProxy(HEART_SRV, SetColor)

    try:
        req = SetColorRequest()
        req.red = red
        req.green = green
        req.blue = blue
        res = heart_srv(req)
    except rospy.ServiceException, e:
        print "Service failed: {}".format(e)

def heart_blink():
    pass
