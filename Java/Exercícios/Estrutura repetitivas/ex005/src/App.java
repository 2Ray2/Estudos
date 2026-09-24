import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

        int n, x, in = 0, out = 0;

        System.out.print("Digite a quantidade de valores: ");
        n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            System.out.print("Digite um valor: ");
            x = sc.nextInt();
            if (x >= 10 && x <= 20) {
                in++;
            }
            
            else {
                out++;
            }
        }   

        System.out.printf("%d in\n", in);
        System.out.printf("%d out", out);
            sc.close();

    }
}
