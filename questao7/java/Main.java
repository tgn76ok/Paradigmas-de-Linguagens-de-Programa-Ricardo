package questao7.java;


public class Main {
    public static void main(String[] args) {
        // Criando escolas
        Escola escola1 = new Escola("Escola A");
        Escola escola2 = new Escola("Escola B");

        // Criando professores
        Professor professor1 = new Professor("Prof. João");
        Professor professor2 = new Professor("Prof. Maria");

        // Associando professores às escolas
        escola1.adicionarProfessor(professor1);
        escola1.adicionarProfessor(professor2);
        escola2.adicionarProfessor(professor1);

        // Listando professores em cada escola
        System.out.println(escola1.listarProfessores());
        System.out.println(escola2.listarProfessores());

        // Listando escolas em que cada professor leciona
        System.out.println(professor1.listarEscolas());
        System.out.println(professor2.listarEscolas());
    }
}