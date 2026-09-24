import java.util.Scanner;

public class ex002 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int x, y, z;

        x = sc.nextInt();
        y = sc.nextInt();
        z = x + y;

        System.out.printf("A soma dos valor %d e %d resulta em %d", x, y, z);
        
        sc.close();
    }
}
