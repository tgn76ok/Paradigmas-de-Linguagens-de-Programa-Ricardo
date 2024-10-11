from abc import ABC, abstractmethod

# Definindo a classe abstrata Imprimivel
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self) -> None:
        pass


# Implementando a classe abstrata na classe Relatorio
class Relatorio(Imprimivel):
    def __init__(self, conteudo: str):
        self.conteudo = conteudo

    def imprimir(self) -> None:
        print(f"Imprimindo Relatório: {self.conteudo}")


# Implementando a classe abstrata na classe Contrato
class Contrato(Imprimivel):
    def __init__(self, partes: str):
        self.partes = partes

    def imprimir(self) -> None:
        print(f"Imprimindo Contrato entre: {self.partes}")


# Testando o código
relatorio = Relatorio("Análise de Vendas")
contrato = Contrato("Empresa X e Empresa Y")

relatorio.imprimir()
contrato.imprimir()
