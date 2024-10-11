from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, especie, nome):
        self.especie = especie
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"


def main():
    cachorro = Cachorro(especie="Canino", nome="Rex")
    gato = Gato(especie="Felino", nome="Mingau")
    
    print(f"O cachorro {cachorro.nome} da espécie {cachorro.especie} faz o som: {cachorro.emitir_som()}")
    print(f"O gato {gato.nome} da espécie {gato.especie} faz o som: {gato.emitir_som()}")


if __name__ == "__main__":
    main()
