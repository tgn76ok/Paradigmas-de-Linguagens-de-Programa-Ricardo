package questao11.java;



// Classe abstrata Funcionario
public abstract class Funcionario {
    protected String nome;

    // Construtor
    public Funcionario(String nome) {
        this.nome = nome;
    }

    // Método abstrato calcularSalario
    public abstract double calcularSalario();
}