class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def ligar(self):
        print(f"O motor de {self.potencia} cavalos a {self.tipo} está ligado.")
        
    def desligar(self):
        print("O motor está desligado.")
        
class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        
    def inflar(self):
        print(f"O pneu {self.marca} de tamanho {self.tamanho} está inflado.")
        
    def desinflar(self):
        print(f"O pneu {self.marca} de tamanho {self.tamanho} está desinflado.")
        
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150)
        self.pneus = [Pneu("Pirelli", 18) for _ in range(4)]  # Criar 4 pneus
        
    def ligar(self):
        self.motor.ligar()
        print(f"O carro {self.marca} {self.modelo} está pronto para rodar.")
        
    def desligar(self):
        self.motor.desligar()  # Corrigido para chamar o método
        print(f"O carro {self.marca} {self.modelo} foi desligado.")
        
    def trocar_pneu(self, indice, novo_pneu):
        if 0 <= indice < len(self.pneus):
            self.pneus[indice] = novo_pneu
            print(f"Pneu {indice + 1} trocado por {novo_pneu.marca} de tamanho {novo_pneu.tamanho}.")
        else:
            print(f"Índice de pneu inválido: {indice + 1}")
            

# Criando uma instância de Carro
carro = Carro("Toyota", "Corolla")

# Ligando o carro
carro.ligar()

# Trocando um pneu
novo_pneu = Pneu("Michelin", 18)  # Corrigido o tamanho para 18
carro.trocar_pneu(2, novo_pneu)   # Trocando o terceiro pneu (índice 2)

# Desligando o carro
carro.desligar()
