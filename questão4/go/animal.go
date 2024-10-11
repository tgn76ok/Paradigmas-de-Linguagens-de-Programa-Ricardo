package main

import "fmt"

// Definindo a interface Animal
type Animal interface {
    Som() string
}

// Estrutura Cachorro
type Cachorro struct {
    nome string
}

// Implementação do método Som para Cachorro
func (c Cachorro) Som() string {
    return fmt.Sprintf("%s faz: Au au!", c.nome)
}

// Estrutura Gato
type Gato struct {
    nome string
}

// Implementação do método Som para Gato
func (g Gato) Som() string {
    return fmt.Sprintf("%s faz: Miau!", g.nome)
}

func main() {
    // Instanciando objetos
    cachorro := Cachorro{"Rex"}
    gato := Gato{"Felix"}

    // Criando uma lista de animais do tipo Animal
    animais := []Animal{cachorro, gato}

    // Exibindo os sons dos animais
    for _, animal := range animais {
        fmt.Println(animal.Som())
    }
}
