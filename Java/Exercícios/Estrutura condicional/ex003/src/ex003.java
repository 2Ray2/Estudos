import java.util.Scanner;

public class ex003 {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            
        int A, B;

        System.out.println("Digite os valores");
        A = sc.nextInt();
        B = sc.nextInt();

        if (A % B == 0)
            System.out.printf("Os numeros %d e %d sao multiplos", A, B);

        else
            System.out.printf("Os numeros %d e %d nao sao multiplos", A, B);

            sc.close();


    }
}
