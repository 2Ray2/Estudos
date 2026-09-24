import java.util.Scanner;

public class ex002 {
    public static void main(String[] args)  {
            Scanner sc = new Scanner(System.in);
            
        int x;

        System.out.println("Digite um numero");

        x = sc.nextInt();

        if (x % 2 == 0)
            System.out.printf("O numero %d e par", x);

        else
            System.out.printf("O numero %d e impar", x);
            
            sc.close();
    }
}
