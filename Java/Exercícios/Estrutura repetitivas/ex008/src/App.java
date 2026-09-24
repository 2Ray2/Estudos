import java.util.Locale;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

        System.out.print("Digite um valor: ");
        int z = 1, x = sc.nextInt();

        if (x == 0) {
            z = 1;
        }

        else {
            for (int i = x; i >= 1; i--) {
                z *= i;
            }
        }
        

        System.out.print(z);
            sc.close();
    }
}