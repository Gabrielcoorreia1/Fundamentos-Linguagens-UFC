# Desafio 7: Implementação de Subprogramas

## Desvendando a "Mágica" da Recursão: A Pilha de Chamadas

A recursão, uma função que chama a si mesma, muitas vezes parece um truque de mágica. Mas, na programação, não há mágica, apenas lógica e estrutura. O segredo por trás da recursão (e, na verdade, de qualquer chamada de função) é uma estrutura de dados fundamental chamada **Pilha de Chamadas** (*Call Stack*).

A pilha funciona como uma pilha de pratos: o último que você coloca é o primeiro que você tira. Cada vez que uma função é chamada, o programa "empurra" um novo bloco de informações para o topo da pilha, contendo as variáveis locais daquela chamada e para onde o código deve retornar.

Para este desafio, decidi visualizar esse processo usando um exemplo clássico de recursão: o cálculo do fatorial de um número.

## O Exemplo: Calculando o Fatorial de um Número

A função fatorial (`n!`) é definida como o produto de todos os números inteiros de 1 a `n`. De forma recursiva, a lógica é: `fatorial(n) = n * fatorial(n-1)`, com o caso base sendo `fatorial(0) = 1`.

O código em Python que implementa essa lógica está no arquivo `fatorial.py`. Para executá-lo:
```bash
python fatorial.py
```

## A Importância da Pilha

Esse mecanismo de empilhar e desempilhar é o que permite que a recursão funcione, garantindo que cada chamada de função tenha seu próprio escopo de variáveis e saiba exatamente para onde voltar. É também por isso que uma recursão infinita causa o famoso erro **"Stack Overflow"**: a pilha de chamadas cresce tanto que estoura o limite de memória reservado para ela.