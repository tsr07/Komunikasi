import socket
import rospy
from std_msgs.msg import Int16
import time

perintah = 0
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addRobot1 = ("192.168.183.175", 9979)
addRobot2 = ("192.168.183.70", 9979)
addRobot3 = ("192.168.183.251", 9979)
delay = 0.5
spam = 5

class Init():
    def __init__(self):
        self.sub_task = rospy.Subscriber("/KRSBI/Comm/Talking", Int16, self.task_callback)
        time.sleep(1)
    
    def task_callback(self, data):
        global perintah
        perintah = data.data
        time.sleep(0)

def kirimRobot1(message):
    pesan = message.encode('utf-8')
    IPsender = addRobot1
    client.sendto(pesan,IPsender)

def kirimRobot2(message):
    pesan = message.encode('utf-8')
    IPsender = addRobot2
    client.sendto(pesan,IPsender)

def kirimRobot3(message):
    pesan = message.encode('utf-8')
    IPsender = addRobot3
    client.sendto(pesan,IPsender)

def commRobot1(ngomong):
    if ngomong == 11:
        for i in range(spam):
            kirimRobot1("com1")
            time.sleep(delay)
    elif ngomong == 12:
        for i in range(spam):
            kirimRobot1("com2")
            time.sleep(delay)
    elif ngomong == 13:
        for i in range(spam):
            kirimRobot1("com3")
            time.sleep(delay)
    elif ngomong == 14:
        for i in range(spam):
            kirimRobot1("com4")
            time.sleep(delay)
    elif ngomong == 15:
        for i in range(spam):
            kirimRobot1("com5")
            time.sleep(delay)
    elif ngomong == 16:
        for i in range(spam):
            kirimRobot1("com6")
            time.sleep(delay)
    elif ngomong == 17:
        for i in range(spam):
            kirimRobot1("com7")
            time.sleep(delay)
    elif ngomong == 18:
        for i in range(spam):
            kirimRobot1("com8")
            time.sleep(delay)
    elif ngomong == 19:
        for i in range(spam):
            kirimRobot1("com9")
            time.sleep(delay)
    elif ngomong == 110:
        for i in range(spam):
            kirimRobot1("com10")
            time.sleep(delay)
    else:
        pass 

def commRobot2(ngomong):
    if ngomong == 21:
        for i in range(spam):
            kirimRobot2("com1")
            time.sleep(delay)
    elif ngomong == 22:
        for i in range(spam):
            kirimRobot2("com2")
            time.sleep(delay)
    elif ngomong == 23:
        for i in range(spam):
            kirimRobot2("com3")
            time.sleep(delay)
    elif ngomong == 24:
        for i in range(spam):
            kirimRobot2("com4")
            time.sleep(delay)
    elif ngomong == 25:
        for i in range(spam):
            kirimRobot2("com5")
            time.sleep(delay)
    elif ngomong == 26:
        for i in range(spam):
            kirimRobot2("com6")
            time.sleep(delay)
    elif ngomong == 27:
        for i in range(spam):
            kirimRobot2("com7")
            time.sleep(delay)
    elif ngomong == 28:
        for i in range(spam):
            kirimRobot2("com8")
            time.sleep(delay)
    elif ngomong == 29:
        for i in range(spam):
            kirimRobot2("com9")
            time.sleep(delay)
    elif ngomong == 210:
        for i in range(spam):
            kirimRobot2("com10")
            time.sleep(delay)
    else:
        pass 

def commRobot3(ngomong):
    if ngomong == 31:
        for i in range(spam):
            kirimRobot3("com1")
            time.sleep(delay)
    elif ngomong == 32:
        for i in range(spam):
            kirimRobot3("com2")
            time.sleep(delay)
    elif ngomong == 33:
        for i in range(spam):
            kirimRobot3("com3")
            time.sleep(delay)
    elif ngomong == 34:
        for i in range(spam):
            kirimRobot3("com4")
            time.sleep(delay)
    elif ngomong == 35:
        for i in range(spam):
            kirimRobot3("com5")
            time.sleep(delay)
    elif ngomong == 36:
        for i in range(spam):
            kirimRobot3("com6")
            time.sleep(delay)
    elif ngomong == 37:
        for i in range(spam):
            kirimRobot3("com7")
            time.sleep(delay)
    elif ngomong == 38:
        for i in range(spam):
            kirimRobot3("com8")
            time.sleep(delay)
    elif ngomong == 39:
        for i in range(spam):
            kirimRobot3("com9")
            time.sleep(delay)
    elif ngomong == 310:
        for i in range(spam):
            kirimRobot3("com10")
            time.sleep(delay)
    elif ngomong == 99:
        kirimRobot3("com99")
        time.sleep(delay)
    else:
        pass

if __name__ == '__main__':
    while not rospy.is_shutdown():
        rospy.init_node("Talker", anonymous=False)
        time.sleep(delay)
        rospy.loginfo("start talking...")
        try:
            perintah = 0
            selesai = False
            while not selesai:
                inisial = Init()
                commRobot1(perintah)
                commRobot2(perintah)
                commRobot3(perintah)
                if perintah >> 0:
                    rospy.loginfo("message was sent")
                    selesai = True
            selesai = False
        except rospy.ROSInterruptException:
            rospy.logerr("ros gagal")
        except rospy.ROSTimeMovedBackwardsException:
            rospy.logerr("ros gagal")