class Retangulo:

    def __init__(self, comprimento, largura):
        if comprimento <= 0 or largura <= 0:
            raise ValueError("O comprimento e a largura devem ser maiores que zero.")
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)


# Criação de uma instância da classe Retangulo
ret = Retangulo(200, 300)

# Cálculo e exibição da área e do perímetro
print(f"Área: {ret.calcular_area()}")        # Saída: Área: 60000
print(f"Perímetro: {ret.calcular_perimetro()}")  # Saída: Perímetro: 
