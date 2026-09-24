import java.util.Scanner;

public class ex003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double r, x, p = 3.14159;

        r = sc.nextDouble();
        x = p * Math.pow(r, 2);

        System.out.printf("A area do circulo com raio igual a %.2f e %.4f", r, x);
        
        sc.close();
    }
}
