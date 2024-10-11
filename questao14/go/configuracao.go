package main

import (
    "fmt"
    "sync"
)

// Struct Configuracao (Singleton)
type Configuracao struct {
    host string
}

var instanciaUnica *Configuracao
var once sync.Once

// Função para retornar a única instância de Configuracao (Singleton)
func GetInstancia() *Configuracao {
    once.Do(func() {
        instanciaUnica = &Configuracao{host: "defaultHost"}
    })
    return instanciaUnica
}

func main() {
    // Testando o Singleton
    config1 := GetInstancia()
    config2 := GetInstancia()

    // Definindo o host na primeira instância
    config1.host = "localhost"

    // Verificando se a outra instância reflete a alteração
    fmt.Println(config2.host)  // Deve imprimir 'localhost'

    // Verificando se config1 e config2 são a mesma instância
    fmt.Println(config1 == config2)  // Deve imprimir 'true'
}
