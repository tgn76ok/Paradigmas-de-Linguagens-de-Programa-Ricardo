class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def amamentar(self):
        print(f"{self.nome} está amamentando seus filhotes.")
        
class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def voar(self):
        print(f"{self.nome} está voando.")
        
class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        super().__init__(nome)  # Usando super() para lidar com a herança múltipla
        
    def emitir_som(self):
        print("Morcego fazendo ruídos noturnos.")
   

# Instanciando o morcego
morcego = Morcego("Batemane")
morcego.emitir_som()      # Método próprio do Morcego
morcego.amamentar()       # Método herdado de Mamifero
morcego.voar()            # Método herdado de Ave
