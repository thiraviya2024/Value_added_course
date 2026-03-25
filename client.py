import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("xxxxxxxxx",9999))
while (True):
    msg=input("enter ur mesg:")
    client.send(msg.encode())
    msg1=client.recv(1024).decode()
    print("server:",msg1)


