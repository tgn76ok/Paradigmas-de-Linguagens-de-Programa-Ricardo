class Configuracao:
    _instancia = None

    # Sobrescrevendo o método __new__ para controlar a criação da instância
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            cls._instancia.configuracao = {}
        return cls._instancia

    def set_parametro(self, chave, valor):
        self.configuracao[chave] = valor

    def get_parametro(self, chave):
        return self.configuracao.get(chave)


# Testando o Singleton
config1 = Configuracao()
config2 = Configuracao()

# Adicionando parâmetros através de uma instância
config1.set_parametro('host', 'localhost')

# Verificando se a outra instância também reflete a alteração
print(config2.get_parametro('host'))  # Deve imprimir 'localhost'

# Verificando se config1 e config2 são a mesma instância
print(config1 is config2)  # Deve imprimir True
