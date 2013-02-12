import socket
dgramSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dgramSock.sendto("192.168.0.200 HAS CONNECTED", ('192.168.0.200',23000))
msg =''

while (msg !='EXIT'):
    msg = raw_input('->')
    if (msg == 'EXIT'):
        dgramSock.sendto('192.168.0.200 IS DISCONECTING', ('192.168.0.200',23000))
    else:
        dgramSock.sendto(msg, ('192.168.0.200',23000))
    

dgramSock.close()
