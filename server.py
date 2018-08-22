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
        port = 9999 #try not to use the common port (for testing)
        s = socket.socket() #s is where /socket or conversation between the computers/servers and target machine.
    except socket.error as msg:
        print("socket creation error: " +str(msg))


#bind socket to port and wait for connection from a client
#where the conversation will take place
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))#you have to convert the port to the string
        s.bind((host, port)) #to bind the socket use bind
        #s.bind((ip address, port ex. "9999")) #call the function "bind", a tuple to a host
        s.listen(3) #listen allows server to accept connections
        #number of bad connections "(#)
    except socket.error as msg:
        print("socket bbinding error: " + str(msg) + "\n" + "retrying.. lol")
        socket_bind() #if fails to bind the socket it will trying until it can bind


#establish a connection with a client (socket must be listening for dem)
#line 30 needs to be there in order to listen before accepting
def socket_accept():
