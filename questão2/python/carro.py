# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para exibir uma descrição detalhada do carro
    def descricao(self):
        return f"Este é um {self.marca} {self.modelo} de {self.ano}"

    # Método para exibir detalhes básicos do carro
    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

# Instanciando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)

# Exibindo a descrição detalhada de cada carro
print(carro1.descricao())
print(carro2.descricao())
