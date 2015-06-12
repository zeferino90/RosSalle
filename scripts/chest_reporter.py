#El from std_msgs.msg import String es necesario para que hable

import rospy
from sensor_msgs.msg import Range
from std_msgs.msg import String	

global pub

def sonar_left_cb(data):
	global pub
	if data.range < 0.29:
		print "Too close of left sonar"
	  	pub.publish(String("left"))	#Necesario para que hable

def sonar_right_cb(data):
	global pub	
	if data.range < 0.29:
		print "Too close of right sonar"
		pub.publish(String("right"))	#Necesario para que hable

if __name__ == "__main__":
	rospy.init_node("chest_reporter_taty", anonymous=True)
	pub = rospy.Publisher('/speech', String)	#Necesario para que hable
	left_sonar_sub = rospy.Subscriber('/nao_robot/sonar/left/sonar', Range, sonar_left_cb)
	right_sonar_sub = rospy.Subscriber('/nao_robot/sonar/right/sonar', Range, sonar_right_cb)
	rospy.spin() #mantiene el programa encendido
