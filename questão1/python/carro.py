# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

# Instanciando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Focus", 2018)

# Exibindo os detalhes de cada carro
print(carro1.detalhes())
print(carro2.detalhes())
print(carro3.detalhes())
