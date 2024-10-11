package questao7.java;

import java.util.ArrayList;
import java.util.List;


public class Professor {
    private String nome;
    private List<Escola> escolas;  // Lista de escolas associadas ao professor

    public Professor(String nome) {
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }

    // Método para associar uma escola ao professor
    public void adicionarEscola(Escola escola) {
        if (!escolas.contains(escola)) {
            escolas.add(escola);
        }
    }

    // Método para listar escolas
    public String listarEscolas() {
        StringBuilder lista = new StringBuilder("Professor " + nome + " leciona em: ");
        for (Escola escola : escolas) {
            lista.append(escola.getNome()).append(", ");
        }
        return lista.toString();
    }

    public String getNome() {
        return nome;
    }
}
