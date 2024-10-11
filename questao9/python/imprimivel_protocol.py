from typing import Protocol

# Definindo o protocolo Imprimivel
class Imprimivel(Protocol):
    def imprimir(self) -> None:
        pass


# Implementando o protocolo na classe Relatorio
class Relatorio:
    def __init__(self, conteudo: str):
        self.conteudo = conteudo

    def imprimir(self) -> None:
        print(f"Imprimindo Relatório: {self.conteudo}")


# Implementando o protocolo na classe Contrato
class Contrato:
    def __init__(self, partes: str):
        self.partes = partes

    def imprimir(self) -> None:
        print(f"Imprimindo Contrato entre: {self.partes}")


# Função que recebe um objeto imprimível
def imprimir_documento(imprimivel: Imprimivel) -> None:
    imprimivel.imprimir()


# Testando o código
relatorio = Relatorio("Análise de Vendas")
contrato = Contrato("Empresa X e Empresa Y")

imprimir_documento(relatorio)
imprimir_documento(contrato)
