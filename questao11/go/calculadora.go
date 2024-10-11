package main

import "fmt"

// Definindo a interface Funcionario
type Funcionario interface {
    CalcularSalario() float64
    Nome() string
}

// Struct FuncionarioHorista que implementa Funcionario
type FuncionarioHorista struct {
    nome            string
    horasTrabalhadas float64
    valorHora       float64
}

// Implementação do método Nome
func (f FuncionarioHorista) Nome() string {
    return f.nome
}

// Implementação do método CalcularSalario
func (f FuncionarioHorista) CalcularSalario() float64 {
    return f.horasTrabalhadas * f.valorHora
}

// Struct FuncionarioAssalariado que implementa Funcionario
type FuncionarioAssalariado struct {
    nome          string
    salarioMensal float64
}

// Implementação do método Nome
func (f FuncionarioAssalariado) Nome() string {
    return f.nome
}

// Implementação do método CalcularSalario
func (f FuncionarioAssalariado) CalcularSalario() float64 {
    return f.salarioMensal
}

func main() {
    // Criando um funcionário horista
    horista := FuncionarioHorista{nome: "João", horasTrabalhadas: 160, valorHora: 25}

    // Criando um funcionário assalariado
    assalariado := FuncionarioAssalariado{nome: "Maria", salarioMensal: 3000}

    // Lista de funcionários
    funcionarios := []Funcionario{horista, assalariado}

    // Calculando e exibindo os salários
    for _, f := range funcionarios {
        fmt.Printf("%s tem salário de: %.2f\n", f.Nome(), f.CalcularSalario())
    }
}
