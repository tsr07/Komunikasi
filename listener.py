import socket
import rospy
from std_msgs.msg import Int8
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = "192.168.183.251"
PORT = 9979
server.bind((IP,PORT))

def menerima():
    global data
    global addr
    data, addr = server.recvfrom(1024)
    print("menerima dari", addr, "pesan: ", data)

def record():
    # ROS Ini
    rospy.init_node("Listener", anonymous=False)
    pub = rospy.Publisher("/KRSBI/Comm/Listening", Int8, queue_size=1)
    time.sleep(1)
    rospy.loginfo("start listening...")
    while not rospy.is_shutdown():
        menerima()
        if data == 'com1':
            rospy.loginfo(data)
            pub.publish(1)
        elif data == 'com2':
            rospy.loginfo(data)
            pub.publish(2)
        elif data == 'com3':
            rospy.loginfo(data)
            pub.publish(3)
        elif data == 'com4':
            rospy.loginfo(data)
            pub.publish(4)
        elif data == 'com5':
            rospy.loginfo(data)
            pub.publish(5)
        elif data == 'com6':
            rospy.loginfo(data)
            pub.publish(6)
        elif data == 'com7':
            rospy.loginfo(data)
            pub.publish(7)
        elif data == 'com8':
            rospy.loginfo(data)
            pub.publish(8)
        elif data == 'com9':
            rospy.loginfo(data)
            pub.publish(9)
        elif data == 'com10':
            rospy.loginfo(data)
            pub.publish(10)

if __name__ == '__main__':
    try:
        record()
    except rospy.ROSInterruptException:
        pass
