package Aula03;

public class Retangulo {
    private double comprimento;
    private double largura;

    // Construtor com validação
    public Retangulo(double comprimento, double largura) {
        if (comprimento <= 0 || largura <= 0) {
            throw new IllegalArgumentException("O comprimento e a largura devem ser maiores que zero.");
        }
        this.comprimento = comprimento;
        this.largura = largura;
    }

    // Método para calcular a área
    public double calcularArea() {
        return comprimento * largura;
    }

    // Método para calcular o perímetro
    public double calcularPerimetro() {
        return 2 * (comprimento + largura);
    }

    // Getters para comprimento e largura
    public double getComprimento() {
        return comprimento;
    }

    public double getLargura() {
        return largura;
    }

    public static void main(String[] args) {
        // Criando uma instância da classe Retangulo com valores válidos
        try {
            Retangulo ret = new Retangulo(200, 300);
            System.out.println("Área: " + ret.calcularArea());
            System.out.println("Perímetro: " + ret.calcularPerimetro());
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        // Exemplo com dimensões inválidas
        try {
            Retangulo retInvalido = new Retangulo(-10, 100);
        } catch (IllegalArgumentException e) {
            System.out.println("Erro ao criar retângulo: " + e.getMessage());
        }
    }
}
