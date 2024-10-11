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

// Função que recebe uma lista de objetos do tipo Animal e chama o método Som
func emitirSons(animais []Animal) {
    for _, animal := range animais {
        fmt.Println(animal.Som())
    }
}

func main() {
    // Instanciando objetos de Cachorro e Gato
    cachorro := Cachorro{nome: "Rex"}
    gato := Gato{nome: "Felix"}
    outroCachorro := Cachorro{nome: "Buddy"}
    outroGato := Gato{nome: "Whiskers"}

    // Criando uma lista de objetos do tipo Animal
    animais := []Animal{cachorro, gato, outroCachorro, outroGato}

    // Chamando a função que demonstra polimorfismo
    emitirSons(animais)
}
