package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
    marca  string
    modelo string
    ano    int
}

// Método para exibir os detalhes do carro
func (c Carro) detalhes() string {
    return fmt.Sprintf("Carro: %s %s, Ano: %d", c.marca, c.modelo, c.ano)
}

func main() {
    // Instanciando objetos da struct Carro
    carro1 := Carro{"Toyota", "Corolla", 2020}
    carro2 := Carro{"Honda", "Civic", 2019}
    carro3 := Carro{"Ford", "Focus", 2018}

    // Exibindo os detalhes de cada carro
    fmt.Println(carro1.detalhes())
    fmt.Println(carro2.detalhes())
    fmt.Println(carro3.detalhes())
}
