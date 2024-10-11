package questão4.java;

public class Gato extends Animal {

    // Construtor da classe Gato
    public Gato(String nome) {
        super(nome); // Chamando o construtor da classe base
    }

    // Sobrescrevendo o método som
    @Override
    public void som() {
        System.out.println(nome + " faz: Miau!");
    }
}