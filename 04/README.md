# Desafio 4: Tipos de Dados

## Uma Análise sobre Tipagem: C, Python e JavaScript

A forma como uma linguagem de programação lida com tipos de dados é uma de suas características mais fundamentais. Ela influencia desde a performance até a segurança do código e a experiência do próprio desenvolvedor. Para explorar essas diferenças, decidi comparar três linguagens que considero um espectro perfeito de abordagens:

* **C:** Representa o controle manual e a rigidez do mundo da programação de sistemas.
* **Python:** Simboliza a flexibilidade e a segurança, priorizando a clareza e a prevenção de erros implícitos.
* **JavaScript:** Famosa por sua onipresença na web e por sua abordagem extremamente permissiva com os tipos.

A análise foca em dois eixos principais: a verificação de tipos (estática vs. dinâmica) e a coerção de tipos (forte vs. fraca).

## Os Conceitos na Prática

Antes de mergulhar nos exemplos, achei importante definir o que esses termos significam no dia a dia da programação:

* **Tipagem Estática vs. Dinâmica:** A questão aqui é *quando* o tipo de uma variável é verificado.
    * **Estática (C):** O tipo é definido no código e verificado durante a compilação. Tentar atribuir um valor de tipo errado gera um erro de compilação.
    * **Dinâmica (Python, JavaScript):** O tipo é associado ao valor, não à variável, e a verificação acontece em tempo de execução. Uma mesma variável pode armazenar um número e, logo depois, um texto.

* **Tipagem Forte vs. Fraca:** Isso se refere ao quão rigorosa a linguagem é ao misturar tipos diferentes em uma operação.
    * **Forte (Python):** A linguagem não permite operações entre tipos incompatíveis. Somar um número com um texto, por exemplo, resulta em um erro claro (`TypeError`).
    * **Fraca (C, JavaScript):** A linguagem tenta "dar um jeito", convertendo um dos tipos para que a operação aconteça. Isso pode ser conveniente, mas também uma fonte de bugs difíceis de rastrear.

## As Linguagens em Ação

Nada melhor do que código para ver como essas teorias se comportam na realidade.

### 1. C: Estática e Fraca

O C exige que você declare o tipo de cada variável, e o compilador garante que você não quebre essa regra. No entanto, ele é surpreendentemente "relaxado" em certas operações.

```c
#include <stdio.h>

int main() {
    int numero = 10;
    // numero = "oi"; // Erro de compilação! Não se pode atribuir string a um int.

    char letra = 'A'; // O valor ASCII de 'A' é 65.

    // Tipagem fraca em ação: C converte 'letra' para int para fazer a soma.
    int resultado = numero + letra; 

    printf("Resultado: %d\n", resultado); // Imprime 75
    return 0;
}
```
O código acima mostra as duas faces do C: a rigidez da declaração de tipos (a linha comentada quebraria a compilação) e a flexibilidade da coerção implícita na operação de soma.

### 2. Python: Dinâmica e Forte

Python oferece total liberdade para trocar o tipo de uma variável, mas jamais permitirá uma operação ambígua sem que o programador a autorize explicitamente.

```python
# Tipagem dinâmica: 'variavel' pode ser o que quisermos.
variavel = 10
print(f"Tipo agora: {type(variavel)}") # <class 'int'>

variavel = "texto"
print(f"Tipo agora: {type(variavel)}") # <class 'str'>

# Tipagem forte: tentar somar int e str resulta em erro.
try:
    resultado = 10 + " Gatos"
except TypeError as e:
    # O erro é explícito e claro, prevenindo bugs.
    print(f"Erro: {e}") 
```
Python nos dá flexibilidade, mas com segurança. Ele confia que o desenvolvedor sabe o que está fazendo, mas o impede de cometer erros óbvios de tipo.

### 3. JavaScript: Dinâmica e Fraca

JavaScript é talvez o exemplo mais famoso de tipagem fraca e dinâmica. Ele tenta, a todo custo, fazer uma operação ter sentido, o que gera comportamentos que são, ao mesmo tempo, úteis e perigosos.

```javascript
// Tipagem dinâmica, como em Python.
let variavel = 10;
variavel = "texto";

// Tipagem fraca em sua forma mais agressiva.
let resultado1 = 10 + "5";    // O número 10 é convertido para string -> "105"
let resultado2 = 10 - "5";    // A string "5" é convertida para número -> 5
let resultado3 = 10 + true;   // O booleano true é convertido para número -> 11

console.log(`10 + "5" = ${resultado1} (tipo: ${typeof resultado1})`);
console.log(`10 - "5" = ${resultado2} (tipo: ${typeof resultado2})`);
console.log(`10 + true = ${resultado3} (tipo: ${typeof resultado3})`);
```
A forma como o JavaScript converte os tipos dependendo do operador (`+` para concatenar, `-` para subtrair) é um exemplo perfeito de sua filosofia flexível, que exige atenção redobrada do programador.
