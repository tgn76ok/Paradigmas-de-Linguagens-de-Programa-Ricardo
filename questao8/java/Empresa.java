package questao8.java;

import java.util.ArrayList;
import java.util.List;

// Classe Empresa
public class Empresa {
    private String nome;
    private List<Empregado> empregados;  // Agregação: lista de empregados

    // Construtor
    public Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    // Método para adicionar um empregado à empresa
    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    // Método para listar todos os empregados da empresa
    public void listarEmpregados() {
        System.out.println("Empresa: " + nome);
        for (Empregado empregado : empregados) {
            System.out.println(empregado.detalhesEmpregado());
        }
    }

    public static void main(String[] args) {
        // Criando empregados
        Empregado empregado1 = new Empregado("Alice", "Desenvolvedora", 8000);
        Empregado empregado2 = new Empregado("Carlos", "Gerente", 12000);

        // Criando uma empresa
        Empresa empresa = new Empresa("TechCorp");

        // Adicionando empregados à empresa
        empresa.adicionarEmpregado(empregado1);
        empresa.adicionarEmpregado(empregado2);

        // Listando os empregados da empresa
        empresa.listarEmpregados();
    }
}