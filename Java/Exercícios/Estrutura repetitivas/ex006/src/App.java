import java.util.Locale;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);
            

        int x;
        double a, b, c;

        System.out.print("Digite a quantidade de casos: ");
        x = sc.nextInt();

        for (int i = 0;i < x;i++) {
            System.out.print("Digite os três valores: ");

            a = sc.nextDouble();
            b = sc.nextDouble();
            c = sc.nextDouble();

            double mp = (a * 2 + b * 3 + c * 5) / (2 + 3 + 5);

            System.out.printf("%.1f\n", mp);
        }

            sc.close();
    }
}
