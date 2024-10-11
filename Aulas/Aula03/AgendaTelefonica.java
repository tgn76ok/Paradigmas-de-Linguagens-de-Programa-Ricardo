package Aula03;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class AgendaTelefonica {

    private static final String FILE_NAME = "contacts.json";
    private static Map<String, String> contacts = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);
    private static Gson gson = new Gson();

    public static void main(String[] args) {
        loadContacts();

        while (true) {
            int choice = showMenuAndGetChoice();

            switch (choice) {
                case 1:
                    addOrEditContact(false); // Adicionar contato
                    break;
                case 2:
                    addOrEditContact(true); // Editar contato
                    break;
                case 3:
                    deleteContact();
                    break;
                case 4:
                    listContacts();
                    break;
                case 5:
                    saveContacts();
                    System.out.println("Saindo...");
                    return;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }

    // Função para mostrar o menu e capturar a escolha do usuário
    private static int showMenuAndGetChoice() {
        System.out.println("\n1. Adicionar contato");
        System.out.println("2. Editar contato");
        System.out.println("3. Excluir contato");
        System.out.println("4. Listar contatos");
        System.out.println("5. Sair");
        System.out.print("Escolha uma opção: ");

        while (!scanner.hasNextInt()) {
            System.out.println("Por favor, insira um número válido.");
            scanner.next(); // Limpa entrada inválida
        }

        int choice = scanner.nextInt();
        scanner.nextLine(); // Consome nova linha
        return choice;
    }

    // Função para adicionar ou editar contato
    private static void addOrEditContact(boolean isEditing) {
        System.out.print(isEditing ? "Nome do contato a ser editado: " : "Nome: ");
        String name = scanner.nextLine();

        if (isEditing && !contacts.containsKey(name)) {
            System.out.println("Contato não encontrado.");
            return;
        }

        System.out.print("Número de telefone (formato: (XX) XXXX-XXXX): ");
        String phone = scanner.nextLine();

        if (validatePhoneNumber(phone)) {
            contacts.put(name, phone);
            System.out.println(isEditing ? "Contato atualizado." : "Contato adicionado.");
        } else {
            System.out.println("Número de telefone inválido.");
        }
    }

    // Função para excluir contato
    private static void deleteContact() {
        System.out.print("Nome do contato a ser excluído: ");
        String name = scanner.nextLine();

        if (contacts.remove(name) != null) {
            System.out.println("Contato excluído.");
        } else {
            System.out.println("Contato não encontrado.");
        }
    }

    // Função para listar os contatos
    private static void listContacts() {
        if (contacts.isEmpty()) {
            System.out.println("Nenhum contato encontrado.");
        } else {
            System.out.println("Contatos:");
            for (Map.Entry<String, String> entry : contacts.entrySet()) {
                System.out.println("Nome: " + entry.getKey() + ", Telefone: " + entry.getValue());
            }
        }
    }

    // Função para validar o formato do número de telefone
    private static boolean validatePhoneNumber(String phone) {
        return phone.matches("\\(\\d{2}\\) \\d{4}-\\d{4}");
    }

    // Função para salvar contatos no arquivo
    private static void saveContacts() {
        try (Writer writer = new FileWriter(FILE_NAME)) {
            gson.toJson(contacts, writer);
            System.out.println("Contatos salvos com sucesso.");
        } catch (IOException e) {
            System.out.println("Erro ao salvar contatos: " + e.getMessage());
        }
    }

    // Função para carregar os contatos do arquivo
    private static void loadContacts() {
        try (Reader reader = new FileReader(FILE_NAME)) {
            Type type = new TypeToken<Map<String, String>>() {}.getType();
            contacts = gson.fromJson(reader, type);
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo de contatos não encontrado. Criando um novo.");
        } catch (IOException e) {
            System.out.println("Erro ao carregar contatos: " + e.getMessage());
        }
    }
}
