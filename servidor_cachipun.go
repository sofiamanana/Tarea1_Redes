package main

import (
	"fmt"
	"net"
	"strings"
	"math/rand"
)

func mensaje_bienvenida() {
	fmt.Printf("Iniciando Servidor\n")
}

func random(){
	fmt.Print(rand.Intn(3),"\n")
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
		fmt.Print("->", string(buffer[0:n]))

		if strings.TrimSpace(string(buffer[0:n])) == "STOP" {
			mensaje := []byte("Me voy byeeee")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
			fmt.Println("ME VOY CHAO")
			return
		} else if strings.TrimSpace(string(buffer[0:n])) == "1"{
			mensaje := []byte("2")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
		}else {
			num_rand := rand.Intn(3)
			if num_rand == 0{
				mensaje := []byte("Piedra")
				_, err = connection.WriteToUDP(mensaje, addr)
				if err != nil {
					fmt.Println(err)
					return
				}
			}else if num_rand == 1{
			mensaje := []byte("Papel")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
			}else if num_rand == 2{
			mensaje := []byte("Tijera")
			_, err = connection.WriteToUDP(mensaje, addr)
			if err != nil {
				fmt.Println(err)
				return
			}
		}
		 
		} 
		
	}
}
