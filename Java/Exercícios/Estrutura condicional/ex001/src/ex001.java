import java.util.Scanner;

public class ex001 {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
        
        int x;

        System.out.println("Digite um numero");

        x = sc.nextInt();
        
        if (x >= 1)
            System.out.printf("O numero %d e NAO NEGATIVO", x);

        else if (x < 0)
            System.out.printf("O numero %d e NEGATIVO", x);
    
            sc.close();
    }
}
