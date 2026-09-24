#include <stdio.h>

int main() {
    int saldo = 1000;
    int valor_saque = 0;
    int nota_100 = 0;
    int nota_50 = 0;
    int nota_20 = 0;
    int nota_10 = 0;
    int nota_5 = 0;

    printf("======Caixa eletronico======\n");
    printf("Seu saldo em conta e R$%d\n", saldo);
    printf("Digite o valor que deseja sacar: ");
    scanf("%d", &valor_saque);

    if (valor_saque % 5 == 0 && valor_saque > 0 && valor_saque <= saldo) {
        while (valor_saque >= 100)
        {
            valor_saque = valor_saque - 100;
            nota_100 += 1;

        }

        while (valor_saque >= 50)
        {
            valor_saque = valor_saque - 50;
            nota_50 += 1;
        }
    
        while (valor_saque >= 20)
        {
            valor_saque = valor_saque - 20;
            nota_20 += 1;
        }
        
        while (valor_saque >= 10)
        {
            valor_saque = valor_saque - 10;
            nota_10 += 1;
        }
        
        while (valor_saque >= 5)
        {
            valor_saque = valor_saque - 5;
            nota_5 += 1;
        }

        printf("======Saque aprovado!======\n");
        printf("Notas de R$100 %d\n", nota_100);
        printf("Notas de R$50 %d\n", nota_50);
        printf("Notas de R$20 %d\n", nota_20);
        printf("Notas de R$10 %d\n", nota_10);
        printf("Notas de R$5 %d", nota_5);
    }

    else {
        if (valor_saque > saldo) {
            printf("Saldo insuficiente.\n");
        }

        else if (valor_saque <= 0) {
            printf("Digite um valor maior que zero.\n");
        }


        else if (valor_saque % 5 != 0) {
            printf("Digite um valor divisivel por cinco. (Termina com zero ou cinco.)\n");
        }
    }
}