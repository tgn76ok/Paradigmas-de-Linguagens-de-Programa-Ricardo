# Exceção personalizada SaldoInsuficienteException
class SaldoInsuficienteException(Exception):
    def __init__(self, message="Saldo insuficiente para realizar o saque"):
        self.message = message
        super().__init__(self.message)


# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Método para saque
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException(f"Saldo insuficiente: Tentativa de saque de {valor}, mas saldo é {self.saldo}")
        self.saldo -= valor
        return self.saldo

    def exibir_saldo(self):
        return self.saldo


# Testando a exceção personalizada
conta = ContaBancaria("João", 500)

try:
    print(f"Saldo atual: {conta.exibir_saldo()}")
    conta.sacar(600)  # Tentativa de saque maior que o saldo
except SaldoInsuficienteException as e:
    print(e)
