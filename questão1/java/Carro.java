package questão1.java;

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

    // Método para exibir os detalhes do carro
    public String detalhes() {
        return "Carro: " + this.marca + " " + this.modelo + ", Ano: " + this.ano;
    }

    // Método principal
    public static void main(String[] args) {
        // Instanciando objetos da classe Carro
        Carro carro1 = new Carro("Toyota", "Corolla", 2020);
        Carro carro2 = new Carro("Honda", "Civic", 2019);
        Carro carro3 = new Carro("Ford", "Focus", 2018);

        // Exibindo os detalhes de cada carro
        System.out.println(carro1.detalhes());
        System.out.println(carro2.detalhes());
        System.out.println(carro3.detalhes());
    }
}
