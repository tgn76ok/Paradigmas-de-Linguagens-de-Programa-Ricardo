package questao7.java;

import java.util.ArrayList;
import java.util.List;

// Classe Escola
public class Escola {
    private String nome;
    private List<Professor> professores;  // Lista de professores associados à escola

    public Escola(String nome) {
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    // Método para associar um professor à escola
    public void adicionarProfessor(Professor professor) {
        if (!professores.contains(professor)) {
            professores.add(professor);
            professor.adicionarEscola(this);  // Associação bidirecional
        }
    }

    // Método para listar professores
    public String listarProfessores() {
        StringBuilder lista = new StringBuilder("Escola " + nome + " tem os seguintes professores: ");
        for (Professor professor : professores) {
            lista.append(professor.getNome()).append(", ");
        }
        return lista.toString();
    }

    public String getNome() {
        return nome;
    }
}
