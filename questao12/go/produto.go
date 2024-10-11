package main

import "fmt"

// Struct Produto
type Produto struct {
    nome  string
    preco float64
}

// Método para somar os preços de dois produtos
func (p Produto) SomarPrecos(outro Produto) float64 {
    return p.preco + outro.preco
}

func main() {
    // Criando dois produtos
    produto1 := Produto{nome: "Produto A", preco: 50.0}
    produto2 := Produto{nome: "Produto B", preco: 30.0}

    // Somando os preços dos dois produtos
    total := produto1.SomarPrecos(produto2)

    fmt.Printf("Soma dos preços: %.2f\n", total)
}
