package questao8.java;


// Classe Empregado
public class Empregado {
    private String nome;
    private String cargo;
    private double salario;

    // Construtor
    public Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    // Método para exibir detalhes do empregado
    public String detalhesEmpregado() {
        return "Nome: " + nome + ", Cargo: " + cargo + ", Salário: " + salario;
    }
}