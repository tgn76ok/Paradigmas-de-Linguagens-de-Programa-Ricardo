package questao6.java;

// Classe Carro com composição de um Motor
public class Carro {
    private String marca;
    private String modelo;
    private Motor motor; // Composição: Carro tem um Motor

    // Construtor
    public Carro(String marca, String modelo, Motor motor) {
        this.marca = marca;
        this.modelo = modelo;
        this.motor = motor;
    }

    // Método para exibir detalhes do carro e do motor
    public String detalhesCarro() {
        return "Carro: " + this.marca + " " + this.modelo + ", " + motor.detalhesMotor();
    }

    // Método principal para testar
    public static void main(String[] args) {
        // Criando um motor
        Motor motor1 = new Motor("V8", 500);

        // Criando um carro com o motor associado
        Carro carro1 = new Carro("Ford", "Mustang", motor1);

        // Exibindo os detalhes do carro
        System.out.println(carro1.detalhesCarro());
    }
}