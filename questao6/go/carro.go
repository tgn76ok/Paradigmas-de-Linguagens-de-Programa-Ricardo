package main

import "fmt"

// Definindo a struct Motor
type Motor struct {
    tipo     string
    potencia int
}

// Método para exibir detalhes do motor
func (m Motor) detalhesMotor() string {
    return fmt.Sprintf("Motor: %s com potência de %d cavalos", m.tipo, m.potencia)
}

// Definindo a struct Carro, que tem um Motor
type Carro struct {
    marca  string
    modelo string
    motor  Motor // Composição: Carro tem um Motor
}

// Método para exibir detalhes do carro
func (c Carro) detalhesCarro() string {
    return fmt.Sprintf("Carro: %s %s, %s", c.marca, c.modelo, c.motor.detalhesMotor())
}

func main() {
    // Criando um motor
    motor1 := Motor{"V8", 500}

    // Criando um carro com o motor associado
    carro1 := Carro{"Ford", "Mustang", motor1}

    // Exibindo os detalhes do carro
    fmt.Println(carro1.detalhesCarro())
}
