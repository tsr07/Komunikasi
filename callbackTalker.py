import rospy
from std_msgs.msg import Int16
import time
from std_msgs.msg import String

trigger = ""
# pub_ManCommand = rospy.Publisher("/KRSBI/Manuvering/Command", String, queue_size = 10)
pub_ngomong = rospy.Publisher("/KRSBI/Comm/Talking", Int16, queue_size = 10)
# pub_saklarNgomong = rospy.Publisher("/KRSBI/Comm/SaklarTalk", Bool, queue_size=10)

def init():
    rospy.init_node("TalkerCallback", anonymous=False) #nodenya ganti Taskontrolnantik
    rospy.Subscriber("/KRSBI/Manuvering/Command", String, trigging)

def trigging(datum):
    global trigger
    trigger = datum.data

def talking(data):
    pub_ngomong.publish(data)
    time.sleep(1)

# def saklar_talking(num):
#     pub_saklarNgomong.publish(num)
#     time.sleep(0.1)

# maju = "maju"
# mundur = "mundur"

if __name__ == '__main__':

    try:
        init()
        while not rospy.is_shutdown():
            # if trigger == "on":
                # saklar_talking(1)
            a = int(input("masukkan angka ke 3: "))
            while True:
                talking(a)
                break
            print("robot maju")
    except rospy.ROSInterruptException():
        pass
