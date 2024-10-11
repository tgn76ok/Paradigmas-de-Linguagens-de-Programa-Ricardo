package main

import (
    "errors"
    "fmt"
)

// Struct ContaBancaria
type ContaBancaria struct {
    titular string
    saldo   float64
}

// Método para saque com tratamento de erro
func (c *ContaBancaria) Sacar(valor float64) error {
    if valor > c.saldo {
        return errors.New(fmt.Sprintf("Saldo insuficiente: Tentativa de saque de %.2f, mas saldo é %.2f", valor, c.saldo))
    }
    c.saldo -= valor
    return nil
}

func (c *ContaBancaria) ExibirSaldo() float64 {
    return c.saldo
}

func main() {
    conta := ContaBancaria{titular: "João", saldo: 500}

    fmt.Printf("Saldo atual: %.2f\n", conta.ExibirSaldo())

    // Tentativa de saque maior que o saldo
    err := conta.Sacar(600)
    if err != nil {
        fmt.Println(err)
    }
}
