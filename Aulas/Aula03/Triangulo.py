class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        if not self._eh_triangulo_valido(lado1, lado2, lado3):
            raise ValueError("Os lados fornecidos não formam um triângulo válido.")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def _eh_triangulo_valido(self, lado1, lado2, lado3):
        # Verifica se a soma de dois lados é sempre maior que o terceiro lado
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


# Demonstração de uso da classe Triangulo
try:
    triangulo = Triangulo(3, 4, 5)
    print(f"Perímetro: {triangulo.calcular_perimetro()}")
    print(f"Tipo: {triangulo.tipo()}")
except ValueError as e:
    print(e)
