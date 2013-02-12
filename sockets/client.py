import socket
dgramSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dgramSock.sendto("Hello World\n", ('192.168.0.200',23000))
print dgramSock.recv(100)
dgramSock.close()
