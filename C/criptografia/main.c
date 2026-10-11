#include <stdio.h>

int main() {
    /*
       Vetores usados para guardar as tabelas de substituição da cifra.
       O primeiro armazena a sequência reorganizada por posições pares e ímpares,
       o segundo guarda o alfabeto após o deslocamento de 7 posições.
    */
    char caracteres_shift_pa[63] = {};
    char caracteres_shift[63] = {};
    /* indice controla a posição atual em que cada caractere será armazenado. */
    int indice = 0;
    /* palavra recebe a entrada do usuário e palavra_criptografada guarda o resultado final. */
    char palavra[41];
    char palavra_criptografada[41];
    /*
       Alfabeto original com 62 caracteres: letras maiúsculas, minúsculas e números.
       Esse conjunto será a base para comparar cada caractere da palavra digitada.
    */
    char caracteres[63] = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    };

    /*
       Lê a palavra digitada pelo usuário e armazena em palavra.
       O %40s limita a leitura para 40 caracteres, evitando estouro de buffer.
    */
    printf("Digite uma palavra: ");
    scanf("%40s", palavra);

    /*
       Constrói a tabela com deslocamento de 7 posições.
       Primeiro, copia os caracteres a partir da posição 7 até o final do alfabeto.
       Depois, acrescenta os 7 primeiros caracteres, fechando o deslocamento circular.
    */
    for (int c = 7; c < 62; c++) {
        caracteres_shift[indice] = caracteres[c];
        indice++;
    }

    for (int c = 0; c < 7; c++) {
        caracteres_shift[indice] = caracteres[c];
        indice++;
    }

    indice = 0;

    /*
       Reorganiza a tabela conforme a sequência de posições pares e ímpares.
       Primeiro são armazenados os índices pares, depois os índices ímpares.
    */
    for (int c = 0; c < 62; c += 2) {
        caracteres_shift_pa[indice] = caracteres_shift[c];
        indice++;
    }

    for (int c = 1; c < 62; c += 2) {
        caracteres_shift_pa[indice] = caracteres_shift[c];
        indice++;
    }

    indice = 0;

    /*
       Percorre cada caractere da palavra e compara com o alfabeto original.
       Quando encontra uma correspondência, guarda na posição equivalente da tabela reorganizada.
    */
    for (int c = 0; palavra[c] != '\0'; c++) {
        for (int r = 0; caracteres_shift_pa[r] != '\0'; r++) {
                if (palavra[c] == caracteres[r]) {
                    palavra_criptografada[indice] = caracteres_shift_pa[r];
                    indice++;
                }
        }

        /*
           O caractere '\0' indica o fim da string em C.
           Ele marca o encerramento da palavra criptografada após cada letra processada.
        */
        palavra_criptografada[indice] = '\0';
    }

    /* Exibe o resultado final da palavra criptografada. */
    printf("Esta e sua palavra criptografada: ");
    printf("%s", palavra_criptografada);

    return 0;
}