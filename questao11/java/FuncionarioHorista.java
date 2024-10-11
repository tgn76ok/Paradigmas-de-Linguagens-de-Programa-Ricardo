package questao11.java;



// Classe derivada FuncionarioHorista
public class FuncionarioHorista extends Funcionario {
    private double horasTrabalhadas;
    private double valorHora;

    // Construtor
    public FuncionarioHorista(String nome, double horasTrabalhadas, double valorHora) {
        super(nome);
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorHora = valorHora;
    }

    // Implementação do método calcularSalario
    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorHora;
    }
}