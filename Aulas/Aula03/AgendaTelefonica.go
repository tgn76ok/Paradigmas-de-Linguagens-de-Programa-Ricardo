package aula03

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
)

const fileName = "contacts.json"

var contacts = make(map[string]string)

func Main() {
	loadContacts()
	for {
		showMenu()

		var choice int
		fmt.Scan(&choice)

		switch choice {
		case 1:
			manageContact(false) // Adicionar contato
		case 2:
			manageContact(true) // Editar contato
		case 3:
			deleteContact()
		case 4:
			listContacts()
		case 5:
			if err := saveContacts(); err != nil {
				fmt.Println("Erro ao salvar contatos:", err)
			} else {
				fmt.Println("Contatos salvos com sucesso. Saindo...")
			}
			return
		default:
			fmt.Println("Opção inválida.")
		}
	}
}

func showMenu() {
	fmt.Println("\nMenu de Contatos")
	fmt.Println("1. Adicionar contato")
	fmt.Println("2. Editar contato")
	fmt.Println("3. Excluir contato")
	fmt.Println("4. Listar contatos")
	fmt.Println("5. Salvar e Sair")
	fmt.Print("Escolha uma opção: ")
}

// Função para adicionar ou editar contato
func manageContact(isEditing bool) {
	var name, phone string

	if isEditing {
		fmt.Print("Nome do contato a ser editado: ")
	} else {
		fmt.Print("Nome do contato a ser adicionado: ")
	}
	fmt.Scan(&name)

	if isEditing {
		if _, exists := contacts[name]; !exists {
			fmt.Println("Contato não encontrado.")
			return
		}
	}

	fmt.Print("Número de telefone (formato: (XX) XXXX-XXXX): ")
	fmt.Scan(&phone)

	if validatePhoneNumber(phone) {
		contacts[name] = phone
		if isEditing {
			fmt.Println("Contato atualizado.")
		} else {
			fmt.Println("Contato adicionado.")
		}
	} else {
		fmt.Println("Número de telefone inválido.")
	}
}

// Função para excluir contato
func deleteContact() {
	var name string
	fmt.Print("Nome do contato a ser excluído: ")
	fmt.Scan(&name)

	if _, exists := contacts[name]; exists {
		delete(contacts, name)
		fmt.Println("Contato excluído.")
	} else {
		fmt.Println("Contato não encontrado.")
	}
}

// Função para listar os contatos
func listContacts() {
	if len(contacts) == 0 {
		fmt.Println("Nenhum contato encontrado.")
		return
	}
	fmt.Println("Lista de Contatos:")
	for name, phone := range contacts {
		fmt.Printf("Nome: %s, Telefone: %s\n", name, phone)
	}
}

// Validação de número de telefone usando regex
func validatePhoneNumber(phone string) bool {
	re := regexp.MustCompile(`^\(\d{2}\) \d{4}-\d{4}$`)
	return re.MatchString(phone)
}

// Função para salvar contatos no arquivo
func saveContacts() error {
	data, err := json.Marshal(contacts)
	if err != nil {
		return err
	}
	err = ioutil.WriteFile(fileName, data, 0644)
	return err
}

// Função para carregar contatos do arquivo
func loadContacts() {
	file, err := os.Open(fileName)
	if err != nil {
		if os.IsNotExist(err) {
			return
		}
		fmt.Println("Erro ao carregar contatos:", err)
		return
	}
	defer file.Close()

	data, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println("Erro ao ler o arquivo de contatos:", err)
		return
	}

	if err := json.Unmarshal(data, &contacts); err != nil {
		fmt.Println("Erro ao decodificar contatos:", err)
	}
}
