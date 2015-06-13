__author__ = 'zeferino'

import rospy
from airos4_msgs.srv import Play


SRV_PLAY = "/airos4/audio/play"

def play_audio(filename=None):

    try:
        rospy.wait_for_service(SRV_PLAY, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Service: " + SRV_PLAY + " does not appear to be running.\nReal exception msg: " + str(e))
        return

    play_srv = rospy.ServiceProxy(SRV_PLAY, Play)

    try:
        play_srv(filename)
    except rospy.ServiceException, e:
            print "Service call failed: %s"%e