package questao6.java;


public class Motor {
    private String tipo;
    private int potencia;

    // Construtor
    public Motor(String tipo, int potencia) {
        this.tipo = tipo;
        this.potencia = potencia;
    }

    // Método para exibir detalhes do motor
    public String detalhesMotor() {
        return "Motor: " + this.tipo + " com potência de " + this.potencia + " cavalos";
    }
}