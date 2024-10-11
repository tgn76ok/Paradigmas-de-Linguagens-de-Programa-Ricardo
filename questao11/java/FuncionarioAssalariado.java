package questao11.java;




// Classe derivada FuncionarioAssalariado
public class FuncionarioAssalariado extends Funcionario {
    private double salarioMensal;

    // Construtor
    public FuncionarioAssalariado(String nome, double salarioMensal) {
        super(nome);
        this.salarioMensal = salarioMensal;
    }

    // Implementação do método calcularSalario
    @Override
    public double calcularSalario() {
        return salarioMensal;
    }
}