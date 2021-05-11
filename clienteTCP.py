import socket as skt 
#Cliente -> se conecta con servidor inter -> TCP (no se corta)

print("Bienvenido a Cachipun!")
print("¿Desea jugar? si o no")
resp = input()
if resp.strip() == "si":
    #se conecta con el server inter
    serverAddr = '127.0.0.1' #IP
    puertoServidor = 50367 #puerto
    socketCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #inicia el socket
    response = 1
    socketCliente.connect((serverAddr,puertoServidor)) #se conecta al server

    #hacer verificacion de puerto y aleatorio

    puntosCliente = 0
    puntosBot = 0

    while (puntosCliente or puntosBot)!=3:
        jugada = input("Piedra, Papel o Tijera?")

        socketCliente.send(jugada.strip().encode()) #manda el mensaje -> write
        response = socketCliente.recv(2048).decode() #recibe mensaje de vuelta -> response
        print("El bot jugó: "+response)
        if (jugada == response):
            print("Empate, el marcador se mantiene igual")
            print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
        else:
            if (jugada== 'Piedra' or 'piedra') and (response== 'Papel'):
                print('El ganador de esta ronda fue el bot')
                puntosBot+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
            elif (response== 'Piedra') and (jugada== 'Papel' or 'papel'):
                print('El ganador de esta ronda fue usted')
                puntosCliente+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
            elif (response== 'Piedra') and (jugada== 'Tijera' or 'tijera'):
                print('El ganador de esta ronda fue usted')
                puntosCliente+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
            elif (jugada== 'Piedra' or 'piedra') and (response== 'Tijera'):
                print("El ganador de esta ronda fue el bot")
                puntosBot+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
            elif (jugada== 'Papel' or 'papel') and (response== 'Tijera'):
                print("El ganador de esta ronda fue el bot")
                puntosBot+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
            elif (response== 'Papel') and (jugada== 'Tijera' or 'tijera'):
                print('El ganador de esta ronda fue usted')
                puntosCliente+=1
                print("El marcador actual es Jugador ", puntosCliente, ", bot ", puntosBot)
    if puntosCliente==3:
        print('El ganador de la partida fue: Jugador')
    else:
        print('El ganador de la partida fue: Bot')
    
    socketCliente.close() #cierra el socket
