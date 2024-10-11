package questao13.java;



public class Matematica {

    // Método estático para calcular o fatorial
    public static int fatorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * fatorial(n - 1);
        }
    }

    public static void main(String[] args) {
        // Testando o método estático
        System.out.println("Fatorial de 5: " + Matematica.fatorial(5));
        System.out.println("Fatorial de 7: " + Matematica.fatorial(7));
    }
}
