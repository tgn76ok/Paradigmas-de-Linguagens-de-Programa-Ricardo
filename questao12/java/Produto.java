package questao12.java;




public class Produto {
    private String nome;
    private double preco;

    // Construtor
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    // Método para somar os preços de dois produtos
    public double somarPrecos(Produto outroProduto) {
        return this.preco + outroProduto.preco;
    }

    // Método para exibir os detalhes do produto
    @Override
    public String toString() {
        return nome + " - Preço: " + preco;
    }

    public static void main(String[] args) {
        // Criando dois produtos
        Produto produto1 = new Produto("Produto A", 50.0);
        Produto produto2 = new Produto("Produto B", 30.0);

        // Somando os preços dos dois produtos
        double total = produto1.somarPrecos(produto2);

        System.out.println("Soma dos preços: " + total);
    }
}