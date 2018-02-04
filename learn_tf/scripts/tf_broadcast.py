import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf
import turtlesim.msg

def pose_callback:
	#do something -Broadcast transform
	br = tf.TransformBroadcaster(msg, turtlename)
	br.SendTransform((msg.x, msg.y, 0), tf.transformations.quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")


if __name__ == "main":
	rospy.init_node("tf_broadcast")
	turtlename = rospy.get_param('~turtle')
	rospy.Subscribe('/%s/pose' % turtlename, turtlesim.msg.pose, pose_callback, turtlename)
	rospy.spin()

