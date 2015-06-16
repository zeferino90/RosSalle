__author__ = 'zeferino'

import rospy
from airos4_msgs.srv import Play, SetString, Say, SayRequest


SRV_PLAY = "/airos4/audio/play"
SRV_PLAY_FILE = "airos4/audio/play_file"
SRV_SAY = "airos4/tts/say"

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

def play_audio_file(filename=None):
    try:
        rospy.wait_for_service(SRV_PLAY_FILE, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Service: " + SRV_PLAY_FILE + " does not appear to be running.\nReal exception msg: " + str(e))
        return

    play_file_srv = rospy.ServiceProxy(SRV_PLAY_FILE, SetString)

    try:
        play_file_srv(filename)
    except rospy.ServiceException, e:
            print "Service call failed: %s"%e

def say(phrase=None):

    try:
        rospy.wait_for_service(SRV_SAY, timeout=5)
    except rospy.ROSException as e:
        rospy.logerr("Service: " + SRV_SAY + " does not appear to be running.\nReal exception msg: " + str(e))
        return

    say_srv = rospy.ServiceProxy(SRV_SAY, Say)

    req = SayRequest()
    req.sentence = phrase
    req.moveMouth = True

    try:
        say_srv(req)
    except rospy.ServiceException, e:
            print "Service call failed: %s"%e