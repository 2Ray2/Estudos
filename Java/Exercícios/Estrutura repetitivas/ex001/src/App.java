import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int senha = 0;

        while (senha != 2002) {
            System.out.print("Digite sua senha: ");
            
            senha = sc.nextInt();
            
            if (senha != 2002) {
                System.out.println("Senha Invalida.");
            }

            else {
                System.out.print("Acesso Permitido.");
            }
        }

            sc.close();
    }
}
