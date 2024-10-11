import random
import json
import re
from typing import List, Dict, Tuple

class Vetor:
    def __init__(self, tamanho: int = 10):
        self.vetor = self._ler_vetor(tamanho)

    def _ler_vetor(self, tamanho: int) -> List[int]:
        vetor = []
        for i in range(tamanho):
            vetor.append(int(input(f"Digite o elemento {i}: ")))
        return vetor

    def calcular_maior_menor(self) -> Tuple[int, int]:
        maior = menor = self.vetor[0]

        for num in self.vetor[1:]:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num

        print(f"O maior elemento do vetor é {maior}.")
        print(f"O menor elemento do vetor é {menor}.")
        return maior, menor

    def calcular_soma(self, x: int, y: int) -> int:
        try:
            soma = self.vetor[x] + self.vetor[y]
            print(f"A soma dos valores nas posições {x} e {y} é {soma}.")
            return soma
        except IndexError:
            print("Índices fora do intervalo do vetor.")
            return 0

    def imprimir(self):
        print("Elementos do vetor:")
        for elemento in self.vetor:
            print(elemento)

class BingoCartela:
    def __init__(self):
        self.cartela = self.gerar_cartela()

    def gerar_cartela(self) -> List[int]:
        numeros = set()
        cartela = []
        while len(cartela) < 5:
            numero = random.randint(0, 99)
            if numero not in numeros:
                numeros.add(numero)
                cartela.append(numero)
        return cartela

    def imprimir_cartela(self):
        print("Cartela de bingo:")
        for numero in self.cartela:
            print(numero)

class Validador:
    @staticmethod
    def validar_numero(numero: str) -> bool:
        padrao = re.compile(r"^\(\d{2}\) \d{5}-\d{4}$")
        return bool(padrao.match(numero))

class Contatos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Contatos, cls).__new__(cls)
            cls._instance.contatos = {}
        return cls._instance

    def coletar_dados(self):
        while True:
            nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
            if nome.lower() == 'sair':
                break

            numero = input("Digite o número de telefone (formato: (11) 12345-6789): ")
            if not Validador.validar_numero(numero):
                print("Número de telefone inválido. Tente novamente.")
                continue

            self.contatos[nome] = numero

    def salvar_em_arquivo(self, nome_arquivo: str):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.contatos, arquivo, indent=4)

    def carregar_do_arquivo(self, nome_arquivo: str):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                self.contatos = json.load(arquivo)
        except FileNotFoundError:
            self.contatos = {}

    def exibir_contatos(self):
        if self.contatos:
            for nome, numero in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {numero}")
        else:
            print("Nenhum contato encontrado.")


def main():
    # Exemplo de uso do Vetor
    vetor = Vetor()
    vetor.imprimir()
    vetor.calcular_maior_menor()
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    vetor.calcular_soma(x, y)

    # Exemplo de uso do BingoCartela
    bingo = BingoCartela()
    bingo.imprimir_cartela()

    # Exemplo de uso dos Contatos
    contatos = Contatos()
    contatos.carregar_do_arquivo('contatos.json')
    contatos.coletar_dados()
    contatos.salvar_em_arquivo('contatos.json')
    contatos.exibir_contatos()

if __name__ == "__main__":
    main()
