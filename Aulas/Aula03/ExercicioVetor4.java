package Aula03;

import java.util.Scanner;

public class ExercicioVetor4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] numbers = new int[6];
        int sumEven = 0;
        int countOdd = 0;

        System.out.println("Digite 6 números inteiros:");

        // Entrada dos números pelo usuário
        for (int i = 0; i < 6; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numbers[i] = scanner.nextInt();
        }

        System.out.print("Números pares digitados: ");
        System.out.print("\nNúmeros ímpares digitados: ");

        // Processamento dos números
        for (int num : numbers) {
            if (num % 2 == 0) {
                System.out.print(num + " ");
                sumEven += num;
            } else {
                System.out.print(num + " ");
                countOdd++;
            }
        }

        // Resultados
        System.out.println("\nSoma dos números pares: " + sumEven);
        System.out.println("Quantidade de números ímpares: " + countOdd);
    }
}
