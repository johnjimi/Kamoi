#got em

import socket #two computer can communicate
import sys # can run system commands

# Create a socket (allows computers to connect)
# Client needs the IP of the server
def socket_create(): #create a function called socket_create
    try: #try/catch
        global host #ip address where you connect to
        global port #port is a way where data is coming in (helps undefentify)
        global s
        host = ''
        port = 9999 #try not to use the common port for testing
        s = socket.socket() #s is where /socket or conversation between the computers/servers and target machine.
    except socket.error as msg:
        print("socket creation error: " +str(msg))


#bind socket to port and wait for connection from a client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))#you have to convert the port to the string
        s.bind((host, port))