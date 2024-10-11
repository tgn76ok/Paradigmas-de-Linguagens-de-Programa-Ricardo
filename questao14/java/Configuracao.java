package questao14.java;

public class Configuracao {
    // Instância única (Singleton)
    private static Configuracao instanciaUnica = null;

    private String host;

    // Construtor privado
    private Configuracao() {
        // Definir valores padrão da configuração
        this.host = "defaultHost";
    }

    // Método público para retornar a única instância
    public static Configuracao getInstancia() {
        if (instanciaUnica == null) {
            instanciaUnica = new Configuracao();
        }
        return instanciaUnica;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public String getHost() {
        return this.host;
    }

    public static void main(String[] args) {
        // Testando o Singleton
        Configuracao config1 = Configuracao.getInstancia();
        Configuracao config2 = Configuracao.getInstancia();

        // Definindo o host na primeira instância
        config1.setHost("localhost");

        // Verificando se a outra instância reflete a alteração
        System.out.println(config2.getHost());  // Deve imprimir 'localhost'

        // Verificando se config1 e config2 são a mesma instância
        System.out.println(config1 == config2);  // Deve imprimir 'true'
    }
}
