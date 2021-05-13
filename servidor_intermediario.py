import socket as skt 
#Se conecta con cliente -> TCP
#Se conecta con servidor -> UDP
#seccion TCP
print("Inicie")

serverPorttcp = 50367 #Puerto TCP

serverSockettcp = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #inicia socket

serverSockettcp.bind(('',serverPorttcp)) 
serverSockettcp.listen(1)

clientSockettcp, clientAddrtcp = serverSockettcp.accept()
#WHILE SUPREMO
flag_suprema = 0
serverAddr = 'localhost' 
serverPort = 50001 
clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM) #inicio socket udp
print("[*] Consultando estado servidores de Cachipun")
while flag_suprema!=1: 

    msg_cliente = clientSockettcp.recv(2048).decode() #recibe 1


    if msg_cliente == "1":
       
        clientSocket.sendto(msg_cliente.encode(),(serverAddr,serverPort))  #manda 1
        msg, addr = clientSocket.recvfrom(2048) #recibe 2
        print(addr)
        #print(msg.decode())
        if msg.decode()!="2":
            msg ="2"
            clientSockettcp.send(msg.encode())
        else:

            msg ="1"
            clientSockettcp.send(msg.encode())
            msg_cliente = clientSockettcp.recv(2048).decode() #recibe jugada de cliente
            print("[*] Los servidores de juegos operativos")

            puntosCliente = 0
            puntosBot = 0
            while msg_cliente!="STOP":
                clientSocket.sendto(msg_cliente.encode(),(serverAddr,serverPort)) #manda jugada a cachipun

                msg, addr = clientSocket.recvfrom(2048)
                ip, puerto = addr
                clientSocket.close()
                #iniciar nueva conexion
                clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)


                msg = msg.decode()
                print("[*] El bot jugó "+str(msg))

                if (msg_cliente == msg):
                    #print("Empate, el marcador se mantiene igual")
                    mensj = "0"
                    clientSockettcp.send(mensj.encode())
                else:
                    if (msg_cliente== 'Piedra' or 'piedra') and (msg== 'Papel'):
                        #puntosBot+=1
                        mensj = "1"
                        clientSockettcp.send(mensj.encode())
                    elif (msg== 'Piedra') and (msg_cliente== 'Papel' or 'papel'):
                        #puntosCliente+=1
                        mensj = "2"
                        clientSockettcp.send(mensj.encode())
                    elif (msg== 'Piedra') and (msg_cliente== 'Tijera' or 'tijera'):
                        #puntosCliente+=1
                        mensj = "2"
                        clientSockettcp.send(mensj.encode())
                    elif (msg_cliente== 'Piedra' or 'piedra') and (msg== 'Tijera'):
                        #puntosBot+=1
                        mensj = "1"
                        clientSockettcp.send(mensj.encode())
                    elif (msg_cliente== 'Papel' or 'papel') and (msg== 'Tijera'):
                        #puntosBot+=1
                        mensj = "1"
                        clientSockettcp.send(mensj.encode())
                    elif (msg== 'Papel') and (msg_cliente== 'Tijera' or 'tijera'):
                        #puntosCliente+=1
                        mensj = "2"
                        clientSockettcp.send(mensj.encode())
                msg_cliente = clientSockettcp.recv(2048).decode() 
                
    else:
        #print("Cliente no quiere jugar")
        msg = "STOP"
        clientSocket.sendto(msg.encode(),(serverAddr,serverPort))
        flag_suprema = 1            

respuesta = "1 2 3 me muero bye"
clientSockettcp.send(respuesta.encode()) #write -> msg
clientSockettcp.close()
    
msg = "STOP"
#toSend = input("Escriba: ")
clientSocket.sendto(msg.encode(),(serverAddr,serverPort))

clientSocket.close()
