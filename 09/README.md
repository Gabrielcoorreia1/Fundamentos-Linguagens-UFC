# Desafio 9: Concorrência

## Resumo

Vivemos em um mundo com computadores que possuem múltiplos núcleos de processamento, capazes de executar várias tarefas simultaneamente. A concorrência é a arte de escrever programas que aproveitam esse poder, permitindo que diferentes partes do nosso código rodem de forma "paralela", sem que uma precise esperar a outra terminar.

Existem duas estratégias principais para alcançar isso: dividir o trabalho em múltiplos **processos** ou em múltiplas **threads**. Embora pareçam similares, a forma como eles gerenciam memória e se comunicam é drasticamente diferente, e entender essa diferença foi o meu foco neste desafio. 


## Meu Exemplo: Simulando Downloads Concorrentes

Para colocar a concorrência em prática, decidi criar um script que simula o download de vários arquivos ao mesmo tempo usando **threads** em Python. 

Escolhi este cenário porque o download é uma tarefa "limitada por I/O" (*I/O-bound*), ou seja, o programa passa a maior parte do tempo esperando uma resposta da rede. É o caso de uso perfeito para threads: enquanto uma thread está ociosa esperando um pacote de dados chegar, o processador pode dar atenção a outra thread que está pronta para trabalhar.

Se o programa rodasse de forma sequencial, o tempo total seria a soma do tempo de todos os downloads. Com threads, o tempo total será próximo ao do download mais demorado, provando que as tarefas ocorreram em paralelo.

O código-fonte completo e comentado está no arquivo `simulador_downloads.py`.

Para executar a simulação:
```bash
python simulador_downloads.py
```