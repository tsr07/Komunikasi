import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = "192.168.183.70"
PORT = 9979
server.bind((IP,PORT))

def menerima():
    global data
    global addr
    data, addr = server.recvfrom(1024)
    print("menerima dari", addr, "pesan: ", data)

if __name__ == '__main__':
    while True:
        menerima()
        if data == 'com99':
            break