package main

import "fmt"

// Função regular para calcular o fatorial
func Fatorial(n int) int {
    if n == 0 || n == 1 {
        return 1
    }
    return n * Fatorial(n-1)
}

func main() {
    // Testando a função de fatorial
    fmt.Println("Fatorial de 5:", Fatorial(5))
    fmt.Println("Fatorial de 7:", Fatorial(7))
}
