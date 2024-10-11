package questão2.java;

public class Carro {
    private String marca;
    private String modelo;
    private int ano;

    // Construtor da classe Carro
    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    // Método para exibir uma descrição detalhada do carro
    public String descricao() {
        return "Este é um " + this.marca + " " + this.modelo + " de " + this.ano;
    }

    // Método para exibir detalhes básicos do carro
    public String detalhes() {
        return "Carro: " + this.marca + " " + this.modelo + ", Ano: " + this.ano;
    }

    // Método principal
    public static void main(String[] args) {
        // Instanciando objetos da classe Carro
        Carro carro1 = new Carro("Toyota", "Corolla", 2020);
        Carro carro2 = new Carro("Honda", "Civic", 2019);

        // Exibindo a descrição detalhada de cada carro
        System.out.println(carro1.descricao());
        System.out.println(carro2.descricao());
    }
}
