#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import socket
import errno
from time import sleep

UDP_IP = "127.0.0.1"
UDP_PORT_READ = 5432
UDP_PORT_WRITE = 5431

sock_read = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
sock_read.bind((UDP_IP, UDP_PORT_READ))
sock_read.setblocking(False)

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

def callback(data):
    global sock, UDP_IP, UDP_PORT_WRITE
    s = str(data.data)
    MESSAGE = s
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_WRITE))
    #rospy.loginfo(rospy.get_caller_id() + "GC message = %s", data.data)

def gc_conn():
	global sock_read, UDP_IP, UDP_PORT_READ
	pub = rospy.Publisher('gc_connector', String, queue_size=10)
	rospy.init_node('gc_conn', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	phase = 0
	rospy.Subscriber("gc_sender", String, callback)
	while not rospy.is_shutdown():
		try:
			data, addr = sock_read.recvfrom(1024)  # buffer size is 1024 bytes
			
		except socket.error, e:
			err = e.args[0]
			if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
				sleep(0.1)
				#print 'No data available'
				continue
			else:
				# a "real" error occurred
				print e
				sys.exit(1)
		else:		
			print("received message: %s" % data)
			ph = int(data.split("|")[0])

			#phase = int(data)
		
		#print("dopo connessione")
				
		if(ph == 1):
			hello_str = "phase recognition"
			rospy.loginfo(hello_str)
			pub.publish(hello_str)
			rate.sleep()

		elif(ph == 2):
			hello_str = "phase execution" + str(data)
			rospy.loginfo(hello_str)
			pub.publish(hello_str)
			rate.sleep()
		elif(ph == 0):
			hello_str = "phase connection"
			rospy.loginfo(hello_str)
			pub.publish(hello_str)
			rate.sleep()
		
		else:
			hello_str = "phase uknown" 
			rospy.loginfo(hello_str)
			pub.publish(hello_str)
			rate.sleep()
		
		

if __name__ == '__main__':
	try:
		gc_conn()
	except rospy.ROSInterruptException:
		pass


