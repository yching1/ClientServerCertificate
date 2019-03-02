# first of all import the socket library 
import socket                
from CA import getTranslatedMessage

mykey = 11

# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on computer for 9500
port = 9500                
  
# Next bind to the port 

s.bind(('', port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
    # Establish connection with client. 
    c, addr = s.accept()      
    print('Got connection from', addr)

    # send a certificate message to the client.
    c.send('im a cert'.encode())
    while(True):
        try: 
            #waiting for something to come from the client
            got_back = c.recv(1024).decode() #decoding it to string from bytes
            msgback = getTranslatedMessage("d",got_back, mykey)
            print ("<<< Message: %s"  %(got_back))
            print ("<<< Decrypted: %s" %(msgback))
            if got_back == "Goodbye":
                print ("Fail to acknowledge host! Client disconnected!")
                print("Closing connection...")
                c.close()
                print("Connection closed.")
            elif msgback == "Goodbye":
                print ("Client asked for disconnection. Bye!")
                print("Closing connection...")
                c.close()
                print("Connection closed.")
            else:
                if str(msgback) == "I am here to serve you!": #
                    msg = "I am glad. Initiate transfer protocol."
                    print (">>> %s " %(msg))
                    msgenc = getTranslatedMessage("e", msg, mykey)
                    print (">>> Encrypted: %s" %(msgenc))
                    c.send(msgenc.encode()) # encoding string to bytes and sending
                else:
                    msg = "Continue transfer protocol."
                    print (">>> %s " %(msg))
                    msgenc = getTranslatedMessage("e", msg, mykey)
                    print (">>> Encrypted: %s" %(msgenc))
                    c.send(msgenc.encode()) # encoding string to bytes and sending
        except Exception as e: #breaking out if interrupted by the user
            break
# Close the connection with the client 
print("Closing connection...")
c.close()
print("Connection closed.")