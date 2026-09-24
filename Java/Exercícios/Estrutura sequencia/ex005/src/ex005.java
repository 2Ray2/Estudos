import java.util.Scanner;
import java.util.Locale;

public class ex005 {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);
        
            int num, horas;
            double valHora, salario;
        
        num = sc.nextInt();
        horas = sc.nextInt();
        valHora = sc.nextDouble();
        
        salario = horas * valHora;
        
        System.out.printf("NUMBER = %d\n", num);
        System.out.printf("SALARY = U$ %.2f\n", salario);
            
            sc.close();
    }
}
