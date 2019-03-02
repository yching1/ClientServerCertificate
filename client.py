# Import socket module 
import socket                
from CA import getTranslatedMessage
from CA import getKey
import time

# Create a socket object 
s = socket.socket()          
  
# Connect to port 9500
port = 9500                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

resp = (s.recv(1024).decode()) 
print("<<< Received: %s" %(resp)) 

if resp == "im a cert":
    masterkey = getKey(resp)
    print("Found server key!")
    msg = "Connect to server from client!"
    print(">>> %s" %(msg))
    msgenc = getTranslatedMessage("e", msg, masterkey)
    print(">>> Encrypted: %s" %(msgenc)) 
    s.send(msgenc.encode())
    resp = (s.recv(1024).decode()) 
    print("<<< Received: %s" %(resp)) 
    msgback = getTranslatedMessage("d", resp, masterkey)
    print("<<< Decrypted: %s" %(msgback)) 

    while(True):
        if msgback == "I am glad. Initiate transfer protocol." or msgback == "Continue transfer protocol.":
                # getting input on what to send to server
                inp = input("Enter what to send to server : ")
                #sending to server, encoding string to bytes which is important to send  to network
                msgenc = getTranslatedMessage("e",inp,masterkey)
                print(">>> Encrypted: %s" %(msgenc))
                s.send(msgenc.encode())
                #receiving from server, decoding byte to string
                data = str(s.recv(1024).decode())
                print("<<< Message: %s" %(data))
                #printing the result sent from server
                msgback = getTranslatedMessage("d", data, masterkey)
                print("<<< Decrypted: %s" %(msgback))
        else:
            print("Goodbye!")
            msg = "Goodbye!"
            s.send(msg.encode())
            s.close()    
else:
    print("Goodbye!")
    msg = "Goodbye!"
    s.send(msg.encode())
    s.close()

