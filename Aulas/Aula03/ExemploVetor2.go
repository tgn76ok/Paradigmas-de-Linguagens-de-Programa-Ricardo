package aula03

import (
	"fmt"
)

func main() {
	// Definindo o vetor de inteiros
	vetor := []int{5, 12, 7, 20, 15, 8, 3, 11, 6, 9}

	// Inicializando variáveis
	soma := 0
	maiorValor := vetor[0]
	menorValor := vetor[0]

	// Iterando sobre os elementos do vetor
	for _, valor := range vetor {
		soma += valor
		if valor > maiorValor {
			maiorValor = valor
		}
		if valor < menorValor {
			menorValor = valor
		}
	}

	// Calculando a média
	media := float64(soma) / float64(len(vetor))

	// Exibindo os resultados
	fmt.Printf("Média: %.2f\n", media)
	fmt.Printf("Maior valor: %d\n", maiorValor)
	fmt.Printf("Menor valor: %d\n", menorValor)
}
