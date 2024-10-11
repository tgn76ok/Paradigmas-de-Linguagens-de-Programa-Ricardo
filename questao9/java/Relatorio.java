package questao9.java;


// Classe Relatorio que implementa a interface Imprimivel
public class Relatorio implements Imprimivel {
    private String conteudo;

    // Construtor
    public Relatorio(String conteudo) {
        this.conteudo = conteudo;
    }

    // Implementação do método imprimir
    @Override
    public void imprimir() {
        System.out.println("Imprimindo Relatório: " + conteudo);
    }
}