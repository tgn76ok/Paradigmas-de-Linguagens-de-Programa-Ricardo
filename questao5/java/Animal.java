package questao5.java;

public class Animal {
    protected String nome;

    // Construtor da classe Animal
    public Animal(String nome) {
        this.nome = nome;
    }

    // Método genérico para som (será sobrescrito nas subclasses)
    public void som() {
        System.out.println("O animal faz algum som.");
    }
}