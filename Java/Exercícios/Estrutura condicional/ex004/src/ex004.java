import java.util.Scanner;

public class ex004 {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

        int ini, fi, dif;

        System.out.println("Digite a hora inicial e a hora final do jogo");
        ini = sc.nextInt();
        fi = sc.nextInt();

        if (ini > fi)
            dif = 24 - (ini - fi);

        else
            dif = 24 - (fi - ini);

        System.out.printf("O JOGO DUROU %d HORA(S)", dif);

            sc.close();
    }
}
