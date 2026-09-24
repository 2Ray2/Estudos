import java.util.Scanner;
import java.util.Locale;

public class ex007 {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);
            
        float x, y;

        x = sc.nextFloat();
        y = sc.nextFloat();

        if (x == 0f && y == 0f)
            System.out.println("Origem");

        if (x > 0 && y > 0)
            System.out.println("Q1");

        if (x > 0 && y < 0)
            System.out.println("Q4");

        if (x < 0 && y < 0)
            System.out.println("Q3");

        if (x < 0 && y > 0)
            System.out.println("Q2");
        
            sc.close();
    }
}
