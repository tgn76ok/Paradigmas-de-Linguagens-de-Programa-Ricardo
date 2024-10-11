package questao15.java;

// Classe ContaBancaria
public class ContaBancaria {
    private String titular;
    private double saldo;

    // Construtor
    public ContaBancaria(String titular, double saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    // Método para saque
    public void sacar(double valor) throws SaldoInsuficienteException {
        if (valor > saldo) {
            throw new SaldoInsuficienteException("Saldo insuficiente: Tentativa de saque de " + valor + ", mas saldo é " + saldo);
        }
        saldo -= valor;
    }

    public double exibirSaldo() {
        return saldo;
    }

    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("João", 500);

        System.out.println("Saldo atual: " + conta.exibirSaldo());

        try {
            // Tentativa de saque maior que o saldo
            conta.sacar(600);
        } catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }
    }
}
