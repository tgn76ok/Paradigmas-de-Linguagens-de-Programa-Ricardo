package aula03

import (
	"fmt"
)

func main() {
	var numbers [6]int
	var sumEven, countOdd int

	// Solicitar números ao usuário
	fmt.Println("Digite 6 números inteiros:")

	for i := 0; i < 6; i++ {
		fmt.Printf("Número %d: ", i+1)
		fmt.Scan(&numbers[i])
	}

	// Percorrendo o array e realizando as operações para pares e ímpares
	fmt.Print("Números pares digitados: ")
	for _, num := range numbers {
		if num%2 == 0 {
			fmt.Print(num, " ")
			sumEven += num
		}
	}
	fmt.Println("\nSoma dos números pares:", sumEven)

	fmt.Print("Números ímpares digitados: ")
	for _, num := range numbers {
		if num%2 != 0 {
			fmt.Print(num, " ")
			countOdd++
		}
	}
	fmt.Println("\nQuantidade de números ímpares:", countOdd)
}
