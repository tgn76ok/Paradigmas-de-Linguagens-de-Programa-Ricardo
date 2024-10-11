package questao9.java;


// Classe Contrato que implementa a interface Imprimivel
public class Contrato implements Imprimivel {
    private String partes;

    // Construtor
    public Contrato(String partes) {
        this.partes = partes;
    }

    // Implementação do método imprimir
    @Override
    public void imprimir() {
        System.out.println("Imprimindo Contrato entre: " + partes);
    }
}