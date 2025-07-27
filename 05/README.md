# Desafio 5: Estruturas de Controle

## A Ideia: Um Mini Jogo de Aventura

Para este desafio, eu queria criar algo um pouco mais interativo do que um simples script. Pensei que um pequeno jogo de aventura em texto seria o cenário perfeito para demonstrar as estruturas de controle em ação, já que a mecânica de um jogo assim depende inteiramente delas.

A premissa é simples: o jogador está preso em um quarto e precisa encontrar uma chave para abrir a porta e escapar. O programa precisa reagir às decisões do jogador, repetir o ciclo de ações até que o jogo termine e ter uma forma de interromper esse ciclo.

## Construindo a Lógica do Jogo

Para que o jogo funcionasse, precisei combinar as três estruturas de controle fundamentais pedidas no desafio. A lógica ficou assim:

* **Estrutura de Repetição (`while`):** O coração do jogo é um loop infinito (`while True`). Ele mantém o jogador "preso" no quarto, apresentando as opções e aguardando uma ação a cada rodada. O jogo só termina quando uma condição interna força a saída desse loop.

* **Estrutura de Seleção (`if`/`elif`/`else`):** É o cérebro do jogo. A cada ação do jogador (como "olhar a mesa" ou "tentar abrir a porta"), uma série de `if`s e `elif`s verifica o que foi digitado e determina a consequência. É essa estrutura que permite a tomada de decisões e dá interatividade à experiência.

* **Controle de Fluxo (`break`):** Essa é a chave de saída, literalmente. Quando o jogador finalmente consegue abrir a porta ou decide desistir, o comando `break` é acionado para interromper o loop `while` e encerrar o programa.

## Código-Fonte e Execução

O código-fonte completo e comentado da aventura está no arquivo `jogo_aventura.py`, neste mesmo diretório.

Para jogar, basta executá-lo com um interpretador Python:
```bash
python jogo_aventura.py
```