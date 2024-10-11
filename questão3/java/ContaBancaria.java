// Definindo a classe ContaBancaria
public class ContaBancaria {
    private String titular;  // Atributo privado
    private double saldo;    // Atributo privado

    // Construtor
    public ContaBancaria(String titular, double saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    // Método para depositar um valor na conta
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de " + valor + " realizado. Saldo atual: " + saldo);
        } else {
            System.out.println("Valor de depósito inválido");
        }
    }

    // Método para sacar um valor da conta
    public void sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de " + valor + " realizado. Saldo atual: " + saldo);
        } else {
            System.out.println("Saldo insuficiente ou valor de saque inválido");
        }
    }

    // Método para exibir o saldo
    public double getSaldo() {
        return saldo;
    }

    // Método principal para testes
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("João", 1000);
        conta.depositar(500);
        conta.sacar(300);
        System.out.println("Saldo final: " + conta.getSaldo());
    }
}
