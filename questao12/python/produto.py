# Classe Produto com sobrecarga do operador +
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Sobrecarga do operador + para somar os preços dos produtos
    def __add__(self, other):
        if isinstance(other, Produto):
            return self.preco + other.preco
        return NotImplemented

    def __str__(self):
        return f"{self.nome} - Preço: {self.preco}"

# Criando dois objetos Produto
produto1 = Produto("Produto A", 50.0)
produto2 = Produto("Produto B", 30.0)

# Somando os preços dos dois produtos
total = produto1 + produto2

print(f"Soma dos preços: {total}")
