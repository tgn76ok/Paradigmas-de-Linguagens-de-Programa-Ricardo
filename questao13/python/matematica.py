class Matematica:
    # Método estático para calcular o fatorial
    @staticmethod
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * Matematica.fatorial(n - 1)


# Testando o método estático
print("Fatorial de 5:", Matematica.fatorial(5))
print("Fatorial de 7:", Matematica.fatorial(7))
