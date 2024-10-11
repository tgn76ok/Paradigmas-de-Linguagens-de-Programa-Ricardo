from Funções import coletar_dados, salvar_em_arquivo, carregar_do_arquivo, exibir_contatos
from Funções import ler_vetor, calcular_maior_menor, imprimir, calcular_soma, gerar_cartela, imprimir_cartela

def menu_principal():
    """
    Exibe o menu principal e lida com as escolhas do usuário.
    """
    print("\nMenu:")
    print("1. Adicionar/Editar Contato")
    print("2. Exibir Contatos")
    print("3. Operações com Vetor")
    print("4. Gerar Cartela de Bingo")
    print("5. Salvar e Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def operacoes_vetor():
    """
    Realiza operações com vetor, como ler valores, calcular soma e exibir maior/menor.
    """
    vetor = ler_vetor()
    imprimir(vetor)
    calcular_soma(vetor)
    calcular_maior_menor(vetor)

def main():
    nome_arquivo = 'agenda_telefonica.json'
    
    # Carregar contatos do arquivo ou criar uma agenda vazia se o arquivo não existir
    contatos = carregar_do_arquivo(nome_arquivo)
    
    while True:
        escolha = menu_principal()

        if escolha == '1':
            # Coleta novos contatos e os adiciona ou edita os existentes
            novos_contatos = coletar_dados()
            contatos.update(novos_contatos)

        elif escolha == '2':
            # Exibe todos os contatos cadastrados
            exibir_contatos(contatos)

        elif escolha == '3':
            # Realiza operações com vetor (ler, calcular soma, maior/menor)
            operacoes_vetor()

        elif escolha == '4':
            # Gera e imprime uma cartela de bingo
            imprimir_cartela()

        elif escolha == '5':
            # Salva os contatos no arquivo e encerra o programa
            try:
                salvar_em_arquivo(contatos, nome_arquivo)
                print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
            except Exception as e:
                print(f"Erro ao salvar os dados: {e}")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
