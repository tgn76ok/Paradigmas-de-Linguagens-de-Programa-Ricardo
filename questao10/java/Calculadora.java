package questao10.java;


public class Calculadora {

    // Método somar que aceita dois números
    public int somar(int a, int b) {
        return a + b;
    }

    // Método somar que aceita três números
    public int somar(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        // Somando dois números
        System.out.println("Soma de 2 números: " + calc.somar(5, 10));

        // Somando três números
        System.out.println("Soma de 3 números: " + calc.somar(5, 10, 15));
    }
}