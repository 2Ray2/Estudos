import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

        int x = 1, y = 1;

        while (x != 0 && y != 0) {
            System.out.print("Digite as cordenadas: ");

            x = sc.nextInt();
            y = sc.nextInt();

            if (x == 0 || y == 0) {
                break;
            }
            
            
            if (x < 0) {
                if (y > 0) {
                    System.out.println("Segundo");
                }

                else {
                    System.out.println("Terceiro");
                }
            }

            else {
                    if (y > 0) {
                        System.out.println("Primeiro");
                    }

                    else {
                        System.out.println("Quarto");
                    }
                }
            }
            
            sc.close();
    }
}
