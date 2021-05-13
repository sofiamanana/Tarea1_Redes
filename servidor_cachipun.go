package main

import (
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"strings"
)

func mensaje_bienvenida() {
	fmt.Printf("[*] Bienvenidos a Servidor Cachipun 2021\n")
}

func random() {
	fmt.Print(rand.Intn(3), "\n")
}

func main() {
	fmt.Printf("[*] Bienvenidos a Servidor Cachipun 2021\n")
	PUERTO := ":50001"
	BUFFER := 1024
	s, err := net.ResolveUDPAddr("udp4", PUERTO)
	if err != nil {
		fmt.Println(err)
		return
	}
	connection, err := net.ListenUDP("udp4", s)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer connection.Close()
	buffer := make([]byte, BUFFER)
	fmt.Printf("[*] El servicio para pedir partidas se ejecutara en el puerto localhost" + PUERTO + "\n")
	for {
		n, addr, err := connection.ReadFromUDP(buffer)
		//fmt.Print("Cliente mando ->", string(buffer[0:n]), "\n")

		if strings.TrimSpace(string(buffer[0:n])) == "STOP" {
			mensaje := []byte("Me voy byeeee")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
			fmt.Println("[*] El cliente quiere cerrar la conexion")
			return
		} else if strings.TrimSpace(string(buffer[0:n])) == "1" {
			fmt.Print("Cliente mando -> PARTIDA \n")
			quiero_jugar := rand.Intn(100)
			if quiero_jugar <= 89 { //quiere jugar
				//puertos 49152-65532
				nuevo_puerto := rand.Intn(16380) + 49152
				nuevo_p := ":" + strconv.Itoa(nuevo_puerto)
				BUFFER := 1024
				s, err := net.ResolveUDPAddr("udp4", nuevo_p)
				if err != nil {
					fmt.Println(err)
					return
				}
				connection, err := net.ListenUDP("udp4", s)
				if err != nil {
					fmt.Println(err)
					return
				}
				defer connection.Close()
				buffer := make([]byte, BUFFER)
				fmt.Printf(string(buffer[0:n]))

				mensaje := []byte("2")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
				fmt.Printf("[*] La partida se esta ejecutando en localhost" + nuevo_p + "\n")

			} else if quiero_jugar > 89 { //no quiero jugar >:c
				mensaje := []byte("3")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}

			}

		} else {
			fmt.Print("Cliente mando -> JUGADA \n")
			num_rand := rand.Intn(3)
			if num_rand == 0 {
				fmt.Print("Enviaremos -> 0 \n")
				mensaje := []byte("Piedra")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
			} else if num_rand == 1 {
				mensaje := []byte("Papel")
				fmt.Print("Enviaremos -> 1 \n")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
			} else if num_rand == 2 {
				mensaje := []byte("Tijera")
				fmt.Print("Enviaremos -> 2 \n")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
			}

		}

	}
}

