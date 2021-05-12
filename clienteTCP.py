import socket as skt 
#Cliente -> se conecta con servidor inter -> TCP (no se corta)
resp = 1
serverAddr = '127.0.0.1' #IP
puertoServidor = 50367 #puerto
socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM) 
socketCliente.connect((serverAddr,puertoServidor)) #se conecta al server
while resp!=0:
    
    print("Bienvenido a Cachipun!")
    print("¿Desea jugar? si o no")
    resp = input()
    if resp.strip() == "si":
        #se conecta con el server inter
        #inicia el socket
        response = "1"
        socketCliente.send(response.encode()) #manda 1
        response = socketCliente.recv(2048).decode().strip() #recibe 1
        if response == "1":
            #hacer verificacion de puerto y aleatorio
            flag = 0

            while flag!=1:
                jugada = input("Piedra, Papel o Tijera?\n")

                socketCliente.send(jugada.strip().encode()) #manda el mensaje -> write
                response = socketCliente.recv(2048).decode().strip() #recibe mensaje de vuelta -> response
                
                if response=="1":
                    flag=1
                    print('El ganador de la partida fue: Jugador')
                elif response =="2":
                    print('El ganador de la partida fue: Bot')
                    flag = 1
        else:
            resp=0
            print("El server no quiere jugar :c")
    else: 
        response = "0"
        
        socketCliente.send(response.encode())
        resp=0
        
socketCliente.close() #cierra el socket

