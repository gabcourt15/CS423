#I could not figure out the command to get the actual code off of the geni vm, so I copied it manually onto a document on my computer to upload.  Hopefully there aren't any typos

#import needed libraries
import socket

#create socket object
s = socket.socket()

#define the port of the server that you wish to connect to
port = 6001

#get the local machine name
host = socket.gethostname()

#connect to the server
s.connect(('128.206.119.14',port))

#let the server know your request
s.send("Please send me the UMKC logo")

with open('received_file', 'wb') as f:
	print 'file opened'
	while True:
		print('receiving data...')
		data=s.recv(1024)
		print('data=%s', (data))
		if not data:
			break
		#write data to file
		f.write(data)
f.close()

#let the client know they have the file
print('Successfully got the file')

#close the connection
print('Connection closed')


