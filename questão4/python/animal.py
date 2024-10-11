# Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    # Método que será sobrescrito nas subclasses
    def som(self):
        pass

# Classe derivada Cachorro
class Cachorro(Animal):
    def som(self):
        return f"{self.nome} faz: Au au!"

# Classe derivada Gato
class Gato(Animal):
    def som(self):
        return f"{self.nome} faz: Miau!"

# Instanciando objetos das classes derivadas
cachorro = Cachorro("Rex")
gato = Gato("Felix")

# Exibindo os sons dos animais
print(cachorro.som())
print(gato.som())
