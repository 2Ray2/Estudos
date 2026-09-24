import java.util.Scanner;
import java.util.Locale;

public class ex005 {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);
           
        float x;
        int y;

        x = sc.nextInt();
        y = sc.nextInt();

        if (x < 6 && x > 0)

            if (x == 1)
                x = 4f;

            else if (x == 2)
                x = 4.5f;

            else if (x == 3)
                x = 5f;

            else if (x == 4)
                x = 2f;

            else if (x == 5)
                x = 1.5f;
            
        else
            System.out.println("Produto inexistente");
            
        System.out.printf("Total: R$ %.2f", x * y);

            sc.close();
    }
}
