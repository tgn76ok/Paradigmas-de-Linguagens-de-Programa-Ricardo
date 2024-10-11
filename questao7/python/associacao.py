# Definindo a classe Professor
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []  # Lista de escolas onde o professor leciona

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)  # Associação bidirecional

    def listar_escolas(self):
        escolas_nomes = [escola.nome for escola in self.escolas]
        return f"Professor {self.nome} leciona em: {', '.join(escolas_nomes)}"


# Definindo a classe Escola
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []  # Lista de professores associados à escola

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def listar_professores(self):
        professores_nomes = [professor.nome for professor in self.professores]
        return f"Escola {self.nome} tem os seguintes professores: {', '.join(professores_nomes)}"


# Criando escolas
escola1 = Escola("Escola A")
escola2 = Escola("Escola B")

# Criando professores
professor1 = Professor("Prof. João")
professor2 = Professor("Prof. Maria")

# Associando professores às escolas
professor1.adicionar_escola(escola1)
professor1.adicionar_escola(escola2)
professor2.adicionar_escola(escola1)

# Listando professores em cada escola
print(escola1.listar_professores())
print(escola2.listar_professores())

# Listando escolas em que cada professor leciona
print(professor1.listar_escolas())
print(professor2.listar_escolas())
