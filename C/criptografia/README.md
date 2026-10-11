# Cifra de Substituição em C

## Descrição

Este projeto implementa uma cifra de substituição em linguagem C, com duas etapas principais de transformação: um deslocamento de 7 posições no alfabeto e uma reorganização dos caracteres em uma sequência baseada em posições pares e ímpares. A ideia é receber uma palavra, percorrer cada caractere e trocar cada letra ou número pelo correspondente da tabela gerada pela cifra.

O programa foi desenvolvido como exercício didático de lógica de programação e manipulação de strings em C. Ele não é uma solução de criptografia segura, apenas uma aplicação acadêmica para aprender estruturas de dados básicas e processamento de caracteres.

## Objetivos de aprendizagem

- Trabalhar com vetores de caracteres para armazenar alfabetos e palavras.
- Utilizar laços de repetição para percorrer elementos de um vetor.
- Aplicar condicionais para comparar caracteres.
- Manipular índices para acessar posições específicas de arrays.
- Entender a estrutura de strings em C e a necessidade do caractere nulo `\0`.
- Desenvolver raciocínio sobre transformação e substituição de caracteres.

## Funcionamento

1. O programa define um alfabeto de 62 caracteres: letras maiúsculas, letras minúsculas e números de 0 a 9.
2. Ele desloca esse alfabeto em 7 posições, movendo os elementos iniciais para o final da sequência.
3. Em seguida, reorganiza a tabela resultante separando os caracteres das posições pares e ímpares, em uma sequência específica.
4. A palavra digitada pelo usuário é lida com `scanf` e cada caractere é comparado com o alfabeto original.
5. Quando uma letra ou número coincide com um valor do alfabeto original, o programa armazena o caractere correspondente da tabela reorganizada na palavra criptografada.
6. Ao final, a string criptografada é exibida na tela.

## Conceitos de C utilizados

- Vetores de caracteres: armazenam o alfabeto, a palavra digitada e a palavra criptografada.
- `scanf`: lê a entrada do usuário, neste caso a palavra em formato textual.
- Laços `for`: percorrem o alfabeto e a palavra para realizar as trocas e as comparações.
- Comparação entre caracteres: usa `==` para verificar se um caractere da palavra corresponde a um caractere do alfabeto original.
- Caractere nulo `\0`: marca o fim de uma string em C e é usado para indicar o encerramento da palavra criptografada.

## Como compilar e executar

No diretório do projeto, utilize o compilador GCC:

```bash
gcc main.c -o main
./main
```

Em sistemas Windows, a execução pode ser feita com:

```bash
gcc main.c -o main.exe
main.exe
```

## Exemplo de execução

A seguir, um exemplo real da execução do algoritmo implementado:

```text
Digite uma palavra: teste
Esta e sua palavra criptografada: kFikF
```

Esse resultado foi obtido pela lógica do programa, aplicando o deslocamento de 7 posições e a reorganização por posições pares e ímpares.

## Estrutura do projeto

A estrutura atual do repositório é a seguinte:

```text
C/
└── criptografia/
    ├── README.md
    ├── main.c
    ├── teste_python.py
    └── output/
        └── main.exe
```

- `main.c`: código principal em C do programa.
- `README.md`: documentação do projeto.
- `teste_python.py`: script auxiliar para verificar a lógica da cifra em Python.
- `output/`: diretório com o executável gerado pelo programa.

## Observação acadêmica

Este projeto foi desenvolvido como atividade prática de aprendizado de lógica de programação e linguagem C, com foco na compreensão de vetores, índices, laços, comparação de caracteres e manipulação de strings em C.
