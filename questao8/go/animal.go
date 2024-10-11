package main

import "fmt"

// Definindo a struct Empregado
type Empregado struct {
    nome    string
    cargo   string
    salario float64
}

// Método para exibir detalhes do empregado
func (e Empregado) detalhesEmpregado() string {
    return fmt.Sprintf("Nome: %s, Cargo: %s, Salário: %.2f", e.nome, e.cargo, e.salario)
}

// Definindo a struct Empresa
type Empresa struct {
    nome      string
    empregados []Empregado  // Agregação: slice de empregados
}

// Método para adicionar um empregado à empresa
func (e *Empresa) adicionarEmpregado(empregado Empregado) {
    e.empregados = append(e.empregados, empregado)
}

// Método para listar todos os empregados da empresa
func (e Empresa) listarEmpregados() {
    fmt.Printf("Empresa: %s\n", e.nome)
    for _, empregado := range e.empregados {
        fmt.Println(empregado.detalhesEmpregado())
    }
}

func main() {
    // Criando empregados
    empregado1 := Empregado{"Alice", "Desenvolvedora", 8000}
    empregado2 := Empregado{"Carlos", "Gerente", 12000}

    // Criando uma empresa
    empresa := Empresa{nome: "TechCorp"}

    // Adicionando empregados à empresa
    empresa.adicionarEmpregado(empregado1)
    empresa.adicionarEmpregado(empregado2)

    // Listando os empregados da empresa
    empresa.listarEmpregados()
}
