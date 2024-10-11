package questão4.java;

public class Cachorro extends Animal {

    // Construtor da classe Cachorro
    public Cachorro(String nome) {
        super(nome); // Chamando o construtor da classe base
    }

    // Sobrescrevendo o método som
    @Override
    public void som() {
        System.out.println(nome + " faz: Au au!");
    }
}