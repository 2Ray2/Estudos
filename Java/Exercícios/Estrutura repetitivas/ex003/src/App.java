import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

        int num = 0, alc = 0, gas = 0, die = 0;

        while (num != 4) {
            
            System.out.print("Digite um valor: ");
            
            num = sc.nextInt();

            if (num == 1) {
                alc += 1;
            }

            else if (num == 2) {
                gas += 1;
            }

            else if (num == 3) {
                die += 1;
            }

            else {
                System.out.println("Digite um valor entre 1-3.");
            }
        }

        System.out.println("Alcool: " + alc);
        System.out.println("Gasolina: " + gas);
        System.out.println("Diesel: " + die);
        System.out.print("Muito Obrigado.");

            sc.close();
    }
}
