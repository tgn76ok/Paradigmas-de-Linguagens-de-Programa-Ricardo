package aula03

import "fmt"

// Definição da struct Retangulo
type Retangulo struct {
	comprimento, largura float64
}

// Função para inicializar um Retângulo (Construtor)
func NovoRetangulo(comprimento, largura float64) Retangulo {
	return Retangulo{comprimento: comprimento, largura: largura}
}

// Método para calcular a área do retângulo
func (r Retangulo) calcularArea() float64 {
	return r.comprimento * r.largura
}

// Método para calcular o perímetro do retângulo
func (r Retangulo) calcularPerimetro() float64 {
	return 2 * (r.comprimento + r.largura)
}

func main() {
	// Inicializando o retângulo usando a função "construtora"
	ret := NovoRetangulo(200, 300)

	// Exibindo a área e o perímetro do retângulo
	fmt.Printf("Área: %.2f\n", ret.calcularArea())
	fmt.Printf("Perímetro: %.2f\n", ret.calcularPerimetro())
}
