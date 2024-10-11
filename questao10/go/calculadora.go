package main

import "fmt"

// Função para somar dois números
func somarDois(a int, b int) int {
    return a + b
}

// Função para somar três números
func somarTres(a int, b int, c int) int {
    return a + b + c
}

func main() {
    // Somando dois números
    fmt.Println("Soma de 2 números:", somarDois(5, 10))

    // Somando três números
    fmt.Println("Soma de 3 números:", somarTres(5, 10, 15))
}
