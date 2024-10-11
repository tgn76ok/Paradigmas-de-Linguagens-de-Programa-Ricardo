class Calculadora:
    # Método para somar dois números
    def somar_dois(self, a, b):
        return a + b

    # Método para somar três números
    def somar_tres(self, a, b, c):
        return a + b + c


# Testando a Calculadora
calc = Calculadora()

# Somando dois números
print("Soma de 2 números:", calc.somar_dois(5, 10))

# Somando três números
print("Soma de 3 números:", calc.somar_tres(5, 10, 15))
