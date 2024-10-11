package main

import "fmt"

// Definindo a struct ContaBancaria
type ContaBancaria struct {
    titular string  // Atributo público
    saldo   float64 // Atributo "privado" ao pacote
}

// Método para criar uma nova conta bancária
func NovaContaBancaria(titular string, saldoInicial float64) *ContaBancaria {
    return &ContaBancaria{titular: titular, saldo: saldoInicial}
}

// Método para depositar um valor na conta
func (c *ContaBancaria) Depositar(valor float64) {
    if valor > 0 {
        c.saldo += valor
        fmt.Printf("Depósito de %.2f realizado. Saldo atual: %.2f\n", valor, c.saldo)
    } else {
        fmt.Println("Valor de depósito inválido")
    }
}

// Método para sacar um valor da conta
func (c *ContaBancaria) Sacar(valor float64) {
    if valor > 0 && valor <= c.saldo {
        c.saldo -= valor
        fmt.Printf("Saque de %.2f realizado. Saldo atual: %.2f\n", valor, c.saldo)
    } else {
        fmt.Println("Saldo insuficiente ou valor de saque inválido")
    }
}

// Método para exibir o saldo
func (c *ContaBancaria) ExibirSaldo() float64 {
    return c.saldo
}

func main() {
    // Criando uma nova conta bancária
    conta := NovaContaBancaria("João", 1000)

    // Realizando operações
    conta.Depositar(500)
    conta.Sacar(300)
    fmt.Printf("Saldo final: %.2f\n", conta.ExibirSaldo())
}
