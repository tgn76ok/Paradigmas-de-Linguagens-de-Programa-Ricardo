# Definindo a classe Motor
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def detalhes_motor(self):
        return f"Motor: {self.tipo} com potência de {self.potencia} cavalos"


# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composição: Carro tem um Motor

    def detalhes_carro(self):
        return f"Carro: {self.marca} {self.modelo}, {self.motor.detalhes_motor()}"


# Criando um objeto Motor
motor1 = Motor("V8", 500)

# Criando um objeto Carro com o motor associado
carro1 = Carro("Ford", "Mustang", motor1)

# Exibindo os detalhes do carro, incluindo os detalhes do motor
print(carro1.detalhes_carro())
