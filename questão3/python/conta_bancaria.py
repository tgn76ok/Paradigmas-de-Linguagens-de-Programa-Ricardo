# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    # Método para depositar um valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor de depósito inválido")

    # Método para sacar um valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido")

    # Método para verificar o saldo
    def exibir_saldo(self):
        return self.__saldo

# Instanciando a classe e realizando operações
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(300)
print(f"Saldo final: {conta.exibir_saldo()}")
