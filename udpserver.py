#I could not figure out the command to get the actual code off of the geni vm, so I copied it manually onto a document on my computer to upload.  Hopefully there aren't any typos
#I'm not sure that this UDP solution is exactly correct


#import needed libraries
import socket

#create a socket object
s = socket.socket(socket.AF_INEt, socket.SOCK_DGRAM)

#reserve port
host='local'
port=10000
buf = 1024
addr = (host, port)

#open the file
f=open("umkc-logo-blue@2x.png", "rb")
data = f.read(buf)
while (data):
	if(s.sendto(data,addr)):
		print("sending...")
		data = f.read(buf)

f.close()
s.close()