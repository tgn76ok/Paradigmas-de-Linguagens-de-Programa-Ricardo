package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
    marca  string
    modelo string
    ano    int
}

// Método para exibir uma descrição detalhada do carro
func (c Carro) descricao() string {
    return fmt.Sprintf("Este é um %s %s de %d", c.marca, c.modelo, c.ano)
}

// Método para exibir detalhes básicos do carro
func (c Carro) detalhes() string {
    return fmt.Sprintf("Carro: %s %s, Ano: %d", c.marca, c.modelo, c.ano)
}

func main() {
    // Instanciando objetos da struct Carro
    carro1 := Carro{"Toyota", "Corolla", 2020}
    carro2 := Carro{"Honda", "Civic", 2019}

    // Exibindo a descrição detalhada de cada carro
    fmt.Println(carro1.descricao())
    fmt.Println(carro2.descricao())
}
