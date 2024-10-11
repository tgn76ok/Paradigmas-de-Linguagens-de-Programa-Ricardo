package questao11.java;


public class Main {
    public static void main(String[] args) {
        // Criando um funcionário horista
        Funcionario horista = new FuncionarioHorista("João", 160, 25);

        // Criando um funcionário assalariado
        Funcionario assalariado = new FuncionarioAssalariado("Maria", 3000);

        // Calculando e exibindo os salários
        System.out.println(horista.nome + " tem salário de: " + horista.calcularSalario());
        System.out.println(assalariado.nome + " tem salário de: " + assalariado.calcularSalario());
    }
}
