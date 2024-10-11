# Definindo a classe Empregado
class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def detalhes_empregado(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}"


# Definindo a classe Empresa
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []  # Agregação: lista de empregados

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def listar_empregados(self):
        print(f"Empresa: {self.nome}")
        for empregado in self.empregados:
            print(empregado.detalhes_empregado())


# Criando empregados
empregado1 = Empregado("Alice", "Desenvolvedora", 8000)
empregado2 = Empregado("Carlos", "Gerente", 12000)

# Criando uma empresa
empresa = Empresa("TechCorp")

# Adicionando empregados à empresa
empresa.adicionar_empregado(empregado1)
empresa.adicionar_empregado(empregado2)

# Listando os empregados da empresa
empresa.listar_empregados()
