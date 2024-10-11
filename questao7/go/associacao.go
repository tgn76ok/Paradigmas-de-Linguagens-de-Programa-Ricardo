package main

import "fmt"

// Struct Professor
type Professor struct {
    nome    string
    escolas []*Escola  // Lista de escolas onde o professor leciona
}

// Método para associar uma escola ao professor
func (p *Professor) adicionarEscola(escola *Escola) {
    p.escolas = append(p.escolas, escola)
    escola.adicionarProfessor(p)  // Associação bidirecional
}

// Método para listar escolas onde o professor leciona
func (p Professor) listarEscolas() string {
    resultado := fmt.Sprintf("Professor %s leciona em: ", p.nome)
    for _, escola := range p.escolas {
        resultado += escola.nome + ", "
    }
    return resultado
}

// Struct Escola
type Escola struct {
    nome       string
    professores []*Professor  // Lista de professores na escola
}

// Método para associar um professor à escola
func (e *Escola) adicionarProfessor(professor *Professor) {
    e.professores = append(e.professores, professor)
}

// Método para listar professores da escola
func (e Escola) listarProfessores() string {
    resultado := fmt.Sprintf("Escola %s tem os seguintes professores: ", e.nome)
    for _, professor := range e.professores {
        resultado += professor.nome + ", "
    }
    return resultado
}

func main() {
    // Criando escolas
    escola1 := &Escola{nome: "Escola A"}
    escola2 := &Escola{nome: "Escola B"}

    // Criando professores
    professor1 := &Professor{nome: "Prof. João"}
    professor2 := &Professor{nome: "Prof. Maria"}

    // Associando professores às escolas
    professor1.adicionarEscola(escola1)
    professor1.adicionarEscola(escola2)
    professor2.adicionarEscola(escola1)

    // Listando professores em cada escola
    fmt.Println(escola1.listarProfessores())
    fmt.Println(escola2.listarProfessores())

    // Listando escolas onde cada professor leciona
    fmt.Println(professor1.listarEscolas())
    fmt.Println(professor2.listarEscolas())
}
