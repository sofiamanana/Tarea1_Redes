# Lab1_Redes

#### Integrantes:
- Sofía Mañana Bañales 201804535-5
- Fernanda Cerda Rojas 201804567-5
    
#### Ejecución:
Se requieren tres terminales distintos:
- Primero, se debe ejecutar el servidor de Go, con el comando go run servidor_cachipun.go
- Segundo, se debe ejecutar el servidor intermediario de python, con python servidor_intermediario.py
- Tercero, se debe ejecutar el cliente,  con python clienteTCP.py

#### Terminales:
- En el terminal del cliente, se le dará la bienvenida al juego, donde se deberá ingresar por pantalla "si" o "no" si se desea o no comenzar una partida. Al comenzar una partida, simplemente se le pedirá una de las opciones del juego Piedra, Papel o Tijeras. Debe ingresar la opción tal como están listadas en el nombre del juego (ej. "Piedra", también funcionará si se escribe "piedra")
- En la terminal del server intermediario se mostrará la respuesta del servidor cachipun, ya que existe un 10% de probabilidad de que el server responda que no puede jugar. Si el server está disponible para jugar, el servidor intermediario mostrará por pantalla las jugadas aleatorias del bot por cada jugada del jugador. Al tener un ganador de la partida, se muestra un mensaje de partida terminada. Esto se hará por cada partida jugada.
- Por último, en el terminal servidor se muestra lo que se recibió de parte del servidor intermediario (previamente enviado por el cliente), se puede recibir PARTIDA, indicando que el cliente quiere jugar o JUGADA, indicando que el jugador hizo una jugada. Se mostrará la respuesta que enviará el servidor mediante "Enviaremos x", donde x puede ser un número entre el 1 y el 3, las que corresponden a las tres opciones del cachipún.
