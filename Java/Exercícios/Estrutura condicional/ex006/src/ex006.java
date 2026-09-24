import java.util.Scanner;
import java.util.Locale;

public class ex006 {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);
            
        float x;

        x = sc.nextFloat();

        if (x > 0 && x < 101){

            if (x <= 25)
                System.out.println("Intervalo [0, 25]");

            if (x > 25 && x <= 50)
                System.out.println("Intervalo [25, 50]");

            if (x > 50 && x <= 75)
                System.out.println("Intervalo [50, 75]");

            if (x > 75 && x <= 100)
                System.out.println("Intervalo [75, 100]");
        }
        else
            System.out.println("Fora do intervalo");

            sc.close();
    }
}
