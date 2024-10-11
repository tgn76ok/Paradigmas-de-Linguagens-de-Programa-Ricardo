package Aula03;

// Exemplo de Vetor 2 em Java - calculando a média dos elementos do vetor
// Mais o maior elemento do vetor e o menor elemento do vetor.

public class ExemploVetor2 {
    public static void main(String[] args) {
        int[] vetor = {5, 12, 7, 20, 15, 8, 3, 11, 6, 9};

        int soma = 0;
        int maiorValor = vetor[0];
        int menorValor = vetor[0];

        // Usando o loop for-each para percorrer o vetor
        for (int valor : vetor) {
            soma += valor;
            if (valor > maiorValor) {
                maiorValor = valor;
            }
            if (valor < menorValor) {
                menorValor = valor;
            }
        }

        // Calculando a média
        double media = (double) soma / vetor.length;

        // Exibindo os resultados
        System.out.println("Média: " + media);
        System.out.println("Maior valor: " + maiorValor);
        System.out.println("Menor valor: " + menorValor);
    }
}
