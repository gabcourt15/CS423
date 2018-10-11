#I could not figure out the command to get the actual code off of the geni vm, so I copied it manually onto a document on my computer to upload.  Hopefully there aren't any typos
#I'm not sure that this UDP solution is exactly correct

#import needed libraries
import socket

#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#reserve and bind the port
host='localhost'
port= 10000
s.bind((host,port))

addr = (host, port)
buf = 1024

#opne the file for receiving
f = open("umkc-logo-blue@2x.png","wb")
data,addr = s.recvfrom(buf)

while(data):
	f.write(data)
	data,addr = s.recvfrom(buf)

f.close()
s.close()