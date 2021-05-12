import socket as skt 
#Se conecta con cliente -> TCP
#Se conecta con servidor -> UDP
#seccion TCP


serverPorttcp = 50367 #Puerto TCP

serverSockettcp = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #inicia socket

serverSockettcp.bind(('',serverPorttcp)) 
serverSockettcp.listen(1)

clientSockettcp, clientAddrtcp = serverSockettcp.accept()
#WHILE SUPREMO
flag_suprema = 0
while flag_suprema!=1:
    serverAddr = 'localhost' 
    serverPort = 50001 

    msg_cliente = clientSockettcp.recv(2048).decode() #recibe 1
    clientSocket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM) #inicio socket udp
    if msg_cliente == "1":
       
        clientSocket.sendto(msg_cliente.encode(),(serverAddr,serverPort))  #manda 1
        msg, addr = clientSocket.recvfrom(2048) #recibe 2
        if msg.decode()!="2":
            print("No quiere jugar el sv")
            msg ="2"
            clientSockettcp.send(msg.encode())
        else:

            msg ="1"
            clientSockettcp.send(msg.encode())
            msg_cliente = clientSockettcp.recv(2048).decode()


            puntosCliente = 0
            puntosBot = 0
            while msg_cliente!="STOP":
                clientSocket.sendto(msg_cliente.encode(),(serverAddr,serverPort))

                msg, addr = clientSocket.recvfrom(2048)
                msg = msg.decode()

                print("Bot jugo: "+msg)
                print("Cliente jugo: "+msg_cliente)
                if (msg_cliente == msg):
                    print("Empate, el marcador se mantiene igual")
                    print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                else:
                    if (msg_cliente== 'Piedra' or 'piedra') and (msg== 'Papel'):
                        print('El ganador de esta ronda fue el bot')
                        puntosBot+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                    elif (msg== 'Piedra') and (msg_cliente== 'Papel' or 'papel'):
                        print('El ganador de esta ronda fue usted')
                        puntosCliente+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                    elif (msg== 'Piedra') and (msg_cliente== 'Tijera' or 'tijera'):
                        print('El ganador de esta ronda fue usted')
                        puntosCliente+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                    elif (msg_cliente== 'Piedra' or 'piedra') and (msg== 'Tijera'):
                        print("El ganador de esta ronda fue el bot")
                        puntosBot+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                    elif (msg_cliente== 'Papel' or 'papel') and (msg== 'Tijera'):
                        print("El ganador de esta ronda fue el bot")
                        puntosBot+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                    elif (msg== 'Papel') and (msg_cliente== 'Tijera' or 'tijera'):
                        print('El ganador de esta ronda fue usted')
                        puntosCliente+=1
                        print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
                if puntosCliente == 3:
                    print("Gano Cliente!!")
                    mensj = "1"
                    clientSockettcp.send(mensj.encode())
                    msg_cliente = clientSockettcp.recv(2048).decode()
                    if msg_cliente=="1":
                        print("waaaaaaaaa")
                        puntosCliente = 0
                        puntosBot = 0
                    else:
                        break
                elif puntosBot == 3:
                    print("Gano Bot!!")
                    mensj = "2"
                    clientSockettcp.send(mensj.encode())
                    msg = clientSockettcp.recv(2048).decode()
                    print(msg)
                    if msg=="1":
                        print("waaaaaaaaa")
                        puntosCliente = 0
                        puntosBot = 0
                    else:
                        break
                    
                clientSockettcp.send(msg.encode())
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

msg, addr = clientSocket.recvfrom(2048)
clientSocket.close()
print(msg.decode())
