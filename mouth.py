__author__ = 'zeferino'

import rospy
from airos4_msgs.srv import MouthPrint, MouthPrintRequest

MOUTH_SRV = "/airos4/mouth/mouth_print"

def mouth_print(to_print):
    try:
        rospy.wait_for_service(MOUTH_SRV, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Service: " + MOUTH_SRV + " does not appear to be running.\nReal exception msg: " + str(e))
        return
    mouth_srv = rospy.ServiceProxy(MOUTH_SRV, MouthPrint)

    try:
        req = MouthPrintRequest()
        req.sentence = to_print
        res = mouth_srv(req)
    except rospy.ServiceException, e:
        print "Service failed: {}".format(e)