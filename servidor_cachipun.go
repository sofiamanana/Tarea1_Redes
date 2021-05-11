package main

import (
	"fmt"
	"net"
	"strings"
)

func mensaje_bienvenida() {
	fmt.Printf("Iniciando Servidor\n")
}

func main() {
	go mensaje_bienvenida()
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
	for {
		n, addr, err := connection.ReadFromUDP(buffer)
		fmt.Print("->", string(buffer[0:n-1]))

		if strings.TrimSpace(string(buffer[0:n])) == "STOP" {
			mensaje := []byte("Me voy byeeee")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
			fmt.Println("ME VOY CHAO")
			return
		}

		mensaje := []byte("Hola")
		//fmt.Printf("data: %s\n", string(mensaje))
		_, err = connection.WriteToUDP(mensaje, addr)
		if err != nil {
			fmt.Println(err)
			return
		}
	}
}
