package questao5.java;

public class Main {
    public static void main(String[] args) {
        // Instanciando objetos das classes derivadas
        Cachorro cachorro = new Cachorro("Rex");
        Gato gato = new Gato("Felix");

        // Exibindo os sons dos animais
        cachorro.som();
        gato.som();
    }
}
