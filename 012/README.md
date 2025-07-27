# Desafio 12: Programação Lógica

## Proposta

O desafio consiste em modelar um pequeno problema lógico, como um quebra-cabeça ou uma genealogia, utilizando uma sintaxe inspirada na linguagem Prolog. O objetivo é demonstrar como representar conhecimento através de fatos e regras lógicas.

## Solução

O problema escolhido para a modelagem foi o de uma **árvore genealógica** simples, pois se adapta perfeitamente ao paradigma lógico. A solução define uma base de conhecimento com fatos (relações diretas) e regras (relações que podem ser inferidas).

A sintaxe utilizada é inspirada no Prolog:
* **Fatos** terminam com um ponto (`.`).
* **Regras** usam `:-` para representar "se".
* A vírgula (`,`) em uma regra significa "e".
* Nomes que começam com letra maiúscula são variáveis.

---

### 1. Base de Conhecimento: Fatos

Os fatos são as informações que declaramos como verdadeiras. Aqui, definimos quem é o `genitor` de quem.

```prolog
% Fato: genitor(Pai/Mãe, Filho/Filha).

genitor(joao, ana).
genitor(maria, ana).
genitor(joao, pedro).
genitor(maria, pedro).
genitor(ana, laura).
genitor(pedro, jorge).