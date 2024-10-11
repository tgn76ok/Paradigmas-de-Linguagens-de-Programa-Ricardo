from abc import ABC, abstractmethod

# Classe abstrata Funcionario
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    # Método abstrato calcularSalario
    @abstractmethod
    def calcularSalario(self):
        pass


# Classe derivada FuncionarioHorista
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horasTrabalhadas, valorHora):
        super().__init__(nome)
        self.horasTrabalhadas = horasTrabalhadas
        self.valorHora = valorHora

    # Implementação do método calcularSalario
    def calcularSalario(self):
        return self.horasTrabalhadas * self.valorHora


# Classe derivada FuncionarioAssalariado
class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, salarioMensal):
        super().__init__(nome)
        self.salarioMensal = salarioMensal

    # Implementação do método calcularSalario
    def calcularSalario(self):
        return self.salarioMensal


# Testando as classes
horista = FuncionarioHorista("João", 160, 25)
assalariado = FuncionarioAssalariado("Maria", 3000)

print(f"{horista.nome} tem salário de: {horista.calcularSalario()}")
print(f"{assalariado.nome} tem salário de: {assalariado.calcularSalario()}")
