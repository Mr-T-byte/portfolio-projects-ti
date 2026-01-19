import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        double num1, num2, resultado;
        char operacao;

        System.out.println("=== CALCULADORA SIMPLES ===");
        System.out.println("Operações disponíveis:");
        System.out.println("  +  → Soma");
        System.out.println("  -  → Subtração");
        System.out.println("  *  → Multiplicação");
        System.out.println("  /  → Divisão");
        System.out.println("===========================\n");

        // Entrada dos números
        System.out.print("Digite o primeiro número: ");
        num1 = entrada.nextDouble();

        System.out.print("Digite a operação (+, -, *, /): ");
        operacao = entrada.next().charAt(0);

        System.out.print("Digite o segundo número: ");
        num2 = entrada.nextDouble();

        System.out.println("---------------------------");

        // Processamento e saída
        switch (operacao) {
            case '+':
                resultado = num1 + num2;
                System.out.printf("%.2f + %.2f = %.2f%n", num1, num2, resultado);
                break;

            case '-':
                resultado = num1 - num2;
                System.out.printf("%.2f - %.2f = %.2f%n", num1, num2, resultado);
                break;

            case '*':
                resultado = num1 * num2;
                System.out.printf("%.2f × %.2f = %.2f%n", num1, num2, resultado);
                break;

            case '/':
                if (num2 == 0) {
                    System.out.println("Erro: Divisão por zero não é permitida!");
                } else {
                    resultado = num1 / num2;
                    System.out.printf("%.2f ÷ %.2f = %.2f%n", num1, num2, resultado);
                }
                break;

            default:
                System.out.println("Operação inválida! Use apenas +, -, * ou /");
        }

        System.out.println("\nFim do programa.");
        entrada.close();
    }
}