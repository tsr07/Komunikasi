from robocup_game_control_data import GAMECONTROLLER_DATA_PORT, RoboCupGameControlData
import socket
import construct
import rospy
import time
from std_msgs.msg import Int8

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SO_REUSEADDR instead of SO_REUSEPORT to work while TCM is running
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('', GAMECONTROLLER_DATA_PORT))

def menerima():
    global msg
    global addr
    global data
    try:
        msg, addr = client.recvfrom(1024)
        parsed = RoboCupGameControlData.parse(msg)
        data = parsed.state   
        # print('state: ', parsed.state)
        # print('menerima dari', addr)
    except construct.core.ConstError :
        pass

def record():
    rospy.init_node("Listener", anonymous=False)
    pub = rospy.Publisher("/KRSBI/Comm/Listener", Int8, queue_size=1)
    time.sleep(0.1)
    print('Starting Listening')
    while not rospy.is_shutdown():
        menerima()
        rospy.loginfo(data)
        # print(tryku)
        pub.publish(data)
        if data == 0:
            print("initialize")
            pub.publish(0)
        elif data == 1:
            print("Ready")
            pub.publish(1)
        elif data == 2:
            print("Set")
            pub.publish(2)
        elif data == 3:
            print("Play")
            pub.publish(3)
        elif data == 4:
            print("Finish")
            pub.publish(4)
        
    
# Setup UDP client
if __name__ == '__main__':
    try:
        record()
    except rospy.ROSInterruptException:
        pass
        