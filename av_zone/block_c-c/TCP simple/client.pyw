# Echo client program
import socket
import time

#HOST = '192.168.66.154'    # The remote host
HOST = '127.0.0.1'
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world')
data = s.recv(1024)
print 'Received', repr(data)
time.sleep(10)


