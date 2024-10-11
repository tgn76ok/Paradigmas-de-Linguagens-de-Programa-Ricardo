class Pessoa:
    def __init__(self, nome, idade):
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if idade < 0:
            raise ValueError("A idade deve ser positiva.")
        self.nome = nome
        self.idade = idade
        self.endereco = None
    
    def adicionar_endereco(self, endereco):
        self.endereco = endereco
    
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereço:")
            print(self.endereco)
        else:
            print("Endereço não disponível")
        print()  # Adiciona uma linha em branco

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        if not rua or not cidade or not estado or not cep:
            raise ValueError("Todos os campos do endereço devem ser preenchidos.")
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        
    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

    def __str__(self):
        return f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}"


class Empresa:
    def __init__(self, nome, cnpj):
        if not nome or not cnpj:
            raise ValueError("O nome e o CNPJ da empresa devem ser preenchidos.")
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []
        
    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        
    def listar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}:\n")
        
        # Exibe os detalhes (endereço, nome, idade) dos funcionários
        for funcionario in self.funcionarios:
            funcionario.mostrar_informacoes()
        
        # Exibe a lista de nomes dos funcionários
        print("Lista de nomes dos funcionários:")
        for funcionario in self.funcionarios:
            print(f"- {funcionario.nome}")
    
    def __str__(self):
        return f"Empresa: {self.nome}, CNPJ: {self.cnpj}"
            

def main():
    endereco1 = Endereco("Av. Principal", "Cidade A", "Estado X", "12345-678")
    pessoa1 = Pessoa("João", 25)
    pessoa1.adicionar_endereco(endereco1)

    endereco2 = Endereco("Av. Abecedário", "Cidade B", "Estado Y", "98765-432")
    pessoa2 = Pessoa("Matheus", 20)
    pessoa2.adicionar_endereco(endereco2)

    empresa = Empresa("Empresa ABC", "12.345.678/0001-99")
    empresa.contratar_funcionario(pessoa1)
    empresa.contratar_funcionario(pessoa2)

    empresa.listar_funcionarios()

if __name__ == "__main__":
    main()
