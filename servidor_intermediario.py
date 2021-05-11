import socket as skt 
#Se conecta con cliente -> TCP
#Se coencta con servidor -> UDP

#seccion TCP

serverPorttcp = 50367 #Puerto TCP

serverSockettcp = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #inicia socket

serverSockettcp.bind(('',serverPorttcp)) 
serverSockettcp.listen(1)

print('Servidor TCP escuchando en: ',serverPorttcp)

clientSockettcp, clientAddrtcp = serverSockettcp.accept()
msg = clientSockettcp.recv(2048).decode() #read
serverAddr = 'localhost' 
serverPort = 50001 

clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM) #inicio socket udp


if msg == "STOP":
    respuesta = "1 2 3 me muero bye"
    clientSockettcp.send(respuesta.encode()) #write -> response
    clientSockettcp.close()
        
    
    #toSend = input("Escriba: ")
    clientSocket.sendto(msg.encode(),(serverAddr,serverPort))

    msg, addr = clientSocket.recvfrom(2048)
    clientSocket.close()
    print(msg.decode())
else:

    clientSocket.sendto(msg.encode(),(serverAddr,serverPort))

    msg, addr = clientSocket.recvfrom(2048)
    clientSocket.close()
    print(msg.decode())
    