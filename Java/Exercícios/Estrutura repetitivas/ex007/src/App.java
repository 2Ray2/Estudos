import java.util.Locale;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

        double x, y, cont;
        int z;

        System.out.print("Digite a quantidade de pares: ");
        z = sc.nextInt();

        for (int i = 0; i < z; i++) {
            System.out.print("Digite os valores: ");

            x = sc.nextDouble();
            y = sc.nextDouble();

            if (y == 0) {
                System.out.println("Divisão impossivel.");
            }

            else {
                cont = x / y;
                System.out.printf("%.1f", cont);
            }
            
        }

            sc.close();
    }
}
