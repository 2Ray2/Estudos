import java.util.Scanner;

public class App {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

        float x;

        System.out.print("Digite o valor do seu salário: ");

        x = sc.nextFloat();

        if (x <= 2000) {
            System.out.println("Isento");
        }

        else if (x <= 3000) {
            System.out.println("8%");
        } 
        
        else if (x <= 4500) {
            System.out.println("18%");
        } 
        
        else {
            System.out.println("28%");
        }

            sc.close();
    }
}
