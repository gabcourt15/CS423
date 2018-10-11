#I could not figure out the command to get the actual code off of the geni vm, so I copied it manually onto a document on my computer to upload.  Hopefully there aren't any typos

#import needed libraries
import socket

#create socket object
s = socket.socket()
print "Socket successfully created"

#reserve a port
port = 6001

#bind to the port
s.bind((socket.gethostname(), port))

#socket into listening mode
s.listen(5)
print "Socket is listening"

#a loop to listen until we interrupt it or an error occurs
while True:
	#Establish connection with client
	c, addr = s.accept()
	print "Got a connection from", addr
	data= c.recv(1024)
	print('Server received', repr(data))

	filename = 'umkc-logo-blue@2x.png'
	f = open(filename, 'rb')
	l = f.read(1024)
	while (l):
		c.send(l)
		print('Sent', rer(l))
		l = f.read(1024)
	f.close()

	print('Done sending')

	#send a thank you message to the client
	c.send("Thank you for connecting")

	#close the connection with the client
	c.close()