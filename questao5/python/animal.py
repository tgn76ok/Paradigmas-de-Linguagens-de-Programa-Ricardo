# Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    # Método genérico para som (será sobrescrito nas subclasses)
    def som(self):
        pass


# Classe derivada Cachorro
class Cachorro(Animal):
    def som(self):
        print(f"{self.nome} faz: Au au!")


# Classe derivada Gato
class Gato(Animal):
    def som(self):
        print(f"{self.nome} faz: Miau!")


# Função que recebe uma lista de objetos do tipo Animal e chama o método som
def emitir_sons(animais):
    for animal in animais:
        animal.som()


# Instanciando objetos das classes derivadas
cachorro = Cachorro("Rex")
gato = Gato("Felix")
outro_cachorro = Cachorro("Buddy")
outro_gato = Gato("Whiskers")

# Criando uma lista de objetos do tipo Animal
animais = [cachorro, gato, outro_cachorro, outro_gato]

# Chamando a função que demonstra polimorfismo
emitir_sons(animais)
