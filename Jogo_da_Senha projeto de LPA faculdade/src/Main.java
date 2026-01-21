import java.util.Random;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int maxTentativas = 0;
        int[] tentativas = new int[4];
        int[] senhaCorreta = gerarSenha();

        telaInicial();
        lerSenha(tentativas);

        for (maxTentativas = 1; maxTentativas <= 10; maxTentativas++ ) {

            if (verificarSenha(senhaCorreta, tentativas)) {
                voceGanhou(senhaCorreta);
                break;

            }
            if (maxTentativas == 10) {
                gameOver(senhaCorreta);


            } else {
                System.out.printf("Chances: %d/10%n ", maxTentativas);
                tenteNovamente(tentativas);
                lerSenha(tentativas);
            }
        }
    }


    public static int[] gerarSenha() {

        Random random = new Random();
        int[] senhaCorreta = new int[4];

        for (int i = 0; i < 4; i++) {
            senhaCorreta[i] = random.nextInt(6) + 1;
        }

        return senhaCorreta;
    }


    public static void lerSenha(int[] tentativas) {
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < tentativas.length; i++) {

            tentativas[i] = input.nextInt();

            while (tentativas[i] > 6 || tentativas[i] < 1) {
                System.out.println("Entrada invalida, insira numeros de 1 a 6: " );
                tentativas[i] = input.nextInt();
            }

            while (tentativas.length > 4) {

                System.out.println("Entrada invalida, insira somente 4 numeros" );
            }

            while (tentativas.length < 4) {

                System.out.println("Entrada insuficiente, insira 4 numeros" );
            }

        }
    }


    public static void telaInicial() {


        System.out.println("============= JOGO DA SENHA =============");
        System.out.println("Insira 4 numeros de 1 a 6 separados por espacos: ");

    }


    public static void tenteNovamente(int[] tentativas) {


        System.out.println("============= X TENTE NOVAMENTE X =============");
        System.out.println("============= Insira 4 numeros de 1 a 6 separados por espacos: =============");

    }


    public static void gameOver(int[] senhaCorreta) {
        System.out.println("============= VOCE PERDEU =============");
        System.out.print("Senha correta: ");
        for (int i = 0; i<senhaCorreta.length;i++) {
            System.out.print(senhaCorreta[i] + " ");
        }
    }


    public static void voceGanhou(int[] senhaCorreta) {
        System.out.println("===== PARABENS, VOCE VENCEU! =====");
        System.out.print("Senha correta: ");
        for (int i = 0; i<senhaCorreta.length;i++) {
            System.out.print(senhaCorreta[i] + " ");
        }
    }




    public static boolean verificarSenha(int[] senhaCorreta, int[] tentativa) {

        int corretos = 0;
        int desviados = 0;
        boolean[] tentativasMarcadas = {false, false, false, false};
        boolean[] senhasMarcadas = {false, false, false, false};

        for (int i = 0; i < 4; i++) {

            if (senhaCorreta[i] == tentativa[i]) {

                senhasMarcadas [i] = true;
                tentativasMarcadas [i] = true;
                corretos++;
            }
        }

        for (int i = 0; i < 4; i++) {

            if (senhasMarcadas[i] == false) {

                for (int k = 0; k < 4; k++) {
                    if (tentativasMarcadas[k] == false && senhaCorreta[i] == tentativa[k]) {

                        tentativasMarcadas[k] = true;
                        desviados++;

                    }
                }
            }
        }

        System.out.printf("Corretos: %d || Desviados: %d%n ",corretos, desviados);

        return corretos == 4;

    }
}