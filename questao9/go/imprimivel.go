package main

import "fmt"

// Definindo a interface Imprimivel
type Imprimivel interface {
    Imprimir()
}

// Definindo a struct Relatorio que implementa Imprimivel
type Relatorio struct {
    conteudo string
}

// Implementação do método Imprimir para Relatorio
func (r Relatorio) Imprimir() {
    fmt.Println("Imprimindo Relatório:", r.conteudo)
}

// Definindo a struct Contrato que implementa Imprimivel
type Contrato struct {
    partes string
}

// Implementação do método Imprimir para Contrato
func (c Contrato) Imprimir() {
    fmt.Println("Imprimindo Contrato entre:", c.partes)
}

func main() {
    // Criando objetos Relatorio e Contrato
    relatorio := Relatorio{conteudo: "Análise de Vendas"}
    contrato := Contrato{partes: "Empresa X e Empresa Y"}

    // Criando uma lista de objetos imprimíveis
    imprimiveis := []Imprimivel{relatorio, contrato}

    // Chamando o método Imprimir para cada objeto
    for _, item := range imprimiveis {
        item.Imprimir()
    }
}
