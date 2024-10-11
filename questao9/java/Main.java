package questao9.java;



public class Main {
    public static void main(String[] args) {
        // Criando objetos Relatorio e Contrato
        Imprimivel relatorio = new Relatorio("Análise de Vendas");
        Imprimivel contrato = new Contrato("Empresa X e Empresa Y");

        // Imprimindo os objetos
        relatorio.imprimir();
        contrato.imprimir();
    }
}