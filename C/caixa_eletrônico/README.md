# Caixa Eletrônico em C

Exercício desenvolvido em linguagem C para simular o funcionamento básico de um caixa eletrônico.

O programa possui um saldo inicial de **R$ 1.000** e permite que o usuário informe um valor para saque. O valor é validado e, caso o saque seja permitido, o programa calcula a quantidade de notas necessárias utilizando as denominações disponíveis.

## Objetivo

Praticar conceitos fundamentais de programação em C, principalmente:

* declaração e inicialização de variáveis;
* entrada e saída de dados com `scanf` e `printf`;
* operadores aritméticos e relacionais;
* estruturas condicionais (`if`, `else if` e `else`);
* estruturas de repetição (`while`);
* validação de dados;
* construção de uma lógica simples de processamento.

## Regras do saque

O saque é aprovado somente quando todas as condições abaixo são atendidas:

* o valor é maior que zero;
* o valor não ultrapassa o saldo disponível;
* o valor é divisível por 5;
* existem notas disponíveis de R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5.

Caso alguma condição não seja atendida, o programa informa o motivo da recusa.

## Como funciona

Primeiro, o programa solicita o valor que o usuário deseja sacar:

```text
Digite o valor que deseja sacar:
```

Em seguida, verifica se o valor é válido.

Se o saque for aprovado, o programa utiliza `while` para retirar do valor restante a maior nota possível, seguindo esta ordem:

```text
R$ 100 → R$ 50 → R$ 20 → R$ 10 → R$ 5
```

Cada vez que uma nota é utilizada, seu respectivo contador é incrementado.

### Exemplo

Para um saque de **R$ 385**:

```text
385 - 100 = 285
285 - 100 = 185
185 - 100 = 85
85  - 50  = 35
35  - 20  = 15
15  - 10  = 5
5   - 5   = 0
```

Resultado:

```text
3 notas de R$100
1 nota de R$50
1 nota de R$20
1 nota de R$10
1 nota de R$5
```

## Conceitos importantes

### `scanf`

Usado para receber o valor digitado pelo usuário:

```c
scanf("%d", &valor_saque);
```

O `%d` indica que será lido um número inteiro (`int`).

### Operador `%`

Utilizado para verificar se o valor é divisível por 5:

```c
valor_saque % 5 == 0
```

Quando o resto da divisão é `0`, o valor é múltiplo de 5.

### `while`

Os laços de repetição são utilizados para determinar quantas notas de cada valor serão necessárias:

```c
while (valor_saque >= 100)
{
    valor_saque = valor_saque - 100;
    nota_100 += 1;
}
```

O processo continua enquanto ainda houver valor suficiente para utilizar aquela denominação.

## Exemplo de execução

### Saque aprovado

```text
======Caixa eletronico======
Seu saldo em conta e R$1000
Digite o valor que deseja sacar: 280
======Saque aprovado!======
Notas de R$100 2
Notas de R$50 1
Notas de R$20 1
Notas de R$10 1
Notas de R$5 0
```

### Saque recusado

```text
Digite o valor que deseja sacar: 13
Digite um valor divisivel por cinco. (Termina com zero ou cinco.)
```

## O que este exercício representa

Este projeto foi desenvolvido como parte de uma atividade proposta pelo professor, com o objetivo de aplicar na prática conceitos fundamentais da linguagem **C** e de lógica de programação.

A atividade utiliza a simulação de um caixa eletrônico como contexto para trabalhar estruturas condicionais, laços de repetição, entrada e saída de dados e manipulação de variáveis.

## Observações

* O saldo é definido diretamente no código e começa em R$ 1.000.
* O programa trabalha apenas com valores inteiros.
* Não há tratamento de centavos.
* As notas disponíveis são limitadas a R$ 100, R$ 50, R$ 20, R$ 10 e R$ 5.
* Este é um exercício educacional e não representa um sistema bancário real.
