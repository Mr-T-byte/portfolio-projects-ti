import java.util.Scanner;

public class Funcionario {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        // Declaração das variáveis
        String nome;
        String cargo;
        double salarioBruto;
        double horasExtras;
        double valorHoraExtra;
        int dependentes;
        double descontoINSS;
        double descontoIR;
        double salarioLiquido;

        System.out.println("=== CADASTRO DE FUNCIONÁRIO ===\n");

        // Entrada de dados
        System.out.print("Nome completo: ");
        nome = teclado.nextLine();

        System.out.print("Cargo: ");
        cargo = teclado.nextLine();

        System.out.print("Salário bruto (R$): ");
        salarioBruto = teclado.nextDouble();

        System.out.print("Horas extras realizadas: ");
        horasExtras = teclado.nextDouble();

        System.out.print("Valor da hora extra (R$): ");
        valorHoraExtra = teclado.nextDouble();

        System.out.print("Número de dependentes: ");
        dependentes = teclado.nextInt();

        // Cálculos
        double valorHorasExtras = horasExtras * valorHoraExtra;
        double salarioComExtras = salarioBruto + valorHorasExtras;

        // INSS simplificado (tabela aproximada 2025)
        if (salarioComExtras <= 1500) {
            descontoINSS = salarioComExtras * 0.08;
        } else if (salarioComExtras <= 3000) {
            descontoINSS = salarioComExtras * 0.09;
        } else {
            descontoINSS = salarioComExtras * 0.11;
        }

        // IR simplificado (muito básico - apenas exemplo)
        double baseIR = salarioComExtras - descontoINSS - (dependentes * 189.59);
        if (baseIR <= 2259.20) {
            descontoIR = 0;
        } else if (baseIR <= 2826.65) {
            descontoIR = baseIR * 0.075 - 169.44;
        } else {
            descontoIR = baseIR * 0.15 - 381.44;
        }

        salarioLiquido = salarioComExtras - descontoINSS - descontoIR;

        // Resultado
        System.out.println("\n========== FOLHA DE PAGAMENTO ==========");
        System.out.println("Funcionário: " + nome.toUpperCase());
        System.out.println("Cargo:       " + cargo);
        System.out.printf("Salário base:      R$ %,.2f%n", salarioBruto);
        System.out.printf("Horas extras:      R$ %,.2f%n", valorHorasExtras);
        System.out.printf("Salário bruto:     R$ %,.2f%n", salarioComExtras);
        System.out.println("----------------------------------------");
        System.out.printf("Desconto INSS:     R$ %,.2f%n", descontoINSS);
        System.out.printf("Desconto IR:       R$ %,.2f%n", descontoIR);
        System.out.println("----------------------------------------");
        System.out.printf("SALÁRIO LÍQUIDO:   R$ %,.2f%n", salarioLiquido);
        System.out.println("========================================\n");

        System.out.println("Obrigado por usar o sistema!");

        teclado.close();
    }
}