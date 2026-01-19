import java.util.Scanner;

public class Cliente {
    private String nome;
    private String email;
    private int idade;

    // Construtor
    public Cliente(String nome, String email, int idade) {
        this.nome = nome;
        this.email = email;
        this.idade = idade;
    }

    // Getters
    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public int getIdade() {
        return idade;
    }

    // Setters
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setIdade(int idade) {
        if (idade > 0) {
            this.idade = idade;
        } else {
            System.out.println("Idade inválida! Mantendo idade anterior.");
        }
    }

    @Override
    public String toString() {
        return "Cliente: " + nome +
                ", Email: " + email +
                ", Idade: " + idade;
    }

    // Método_principal_com_input_para_interação_do cliente
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Cadastro de Cliente ===");
        System.out.println("Digite os dados do cliente:\n");

        // Leitura do nome
        System.out.print("Nome: ");
        String nome = scanner.nextLine().trim();

        // Leitura do email
        System.out.print("Email: ");
        String email = scanner.nextLine().trim();

        // Leitura da idade com validação básica
        int idade = 0;
        boolean idadeValida = false;

        while (!idadeValida) {
            System.out.print("Idade: ");
            try {
                idade = Integer.parseInt(scanner.nextLine().trim());
                if (idade > 0) {
                    idadeValida = true;
                } else {
                    System.out.println("A idade deve ser maior que zero. Tente novamente.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Por favor, digite apenas números para a idade.");
            }
        }

        // Criando o objeto Cliente
        Cliente cliente = new Cliente(nome, email, idade);

        System.out.println("\n=== Dados cadastrados com sucesso! ===");
        System.out.println(cliente);  // usa o toString()

        // Exemplo de uso dos getters
        System.out.println("\nInformações separadas:");
        System.out.println("Nome:  " + cliente.getNome());
        System.out.println("Email: " + cliente.getEmail());
        System.out.println("Idade: " + cliente.getIdade());

        // Exemplo de alteração com setter
        System.out.print("\nDeseja alterar a idade? (digite nova idade ou Enter para pular): ");
        String novaIdadeStr = scanner.nextLine().trim();

        if (!novaIdadeStr.isEmpty()) {
            try {
                int novaIdade = Integer.parseInt(novaIdadeStr);
                cliente.setIdade(novaIdade);
                System.out.println("Idade atualizada: " + cliente.getIdade());
                System.out.println("Cliente atualizado: " + cliente);
            } catch (NumberFormatException e) {
                System.out.println("Idade inválida. Não foi alterada.");
            }
        }

        System.out.println("\nPrograma finalizado. Obrigado!");
        scanner.close();
    }
}