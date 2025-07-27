# Desafio 10: Gerenciamento de Memória

## Resumo

Quando nosso programa cria variáveis e objetos, eles precisam de um espaço para "viver" na memória RAM do computador. O gerenciamento de memória é o processo de reservar esse espaço (alocação) e, tão importante quanto, liberá-lo quando não é mais necessário (desalocação). Se a memória não for liberada, o programa pode sofrer de "vazamentos de memória" (*memory leaks*), consumindo cada vez mais recursos até travar o sistema.

A grande questão que diferentes linguagens buscam responder é: *quem* deve ter a responsabilidade por esse gerenciamento? O programador ou a própria linguagem? Para explorar as duas respostas para essa pergunta, decidi comparar duas linguagens que representam os extremos dessa filosofia: **C** e **Java**, conforme sugerido na proposta do trabalho.

### C: O Gerenciamento Manual do Artesão

Em C, a filosofia é de controle total e responsabilidade total. A linguagem te dá as ferramentas, e você, o "artesão", é responsável por cada detalhe.

* **Como funciona:** Você precisa pedir explicitamente ao sistema operacional por um bloco de memória usando funções como `malloc()` (alocação de memória). O sistema te entrega um "ponteiro", que é o endereço para esse bloco. Quando você termina de usar essa memória, é sua obrigação devolvê-la usando a função `free()`.
* **A consequência:** Isso dá um poder imenso e permite otimizações de performance incríveis. No entanto, o risco é altíssimo. Esquecer um `free()` causa um vazamento de memória. Usar um ponteiro para uma memória que já foi liberada (*dangling pointer*) pode causar falhas de segurança catastróficas.

### Java: O Gerenciamento Automático do Autômato

Em Java, a filosofia é de segurança e produtividade. A linguagem assume a responsabilidade para que o programador possa focar na lógica de negócio.

* **Como funciona:** Você simplesmente cria objetos com a palavra-chave `new`, e a Máquina Virtual do Java (JVM) se encarrega de alocar a memória necessária. Nos bastidores, um processo chamado **Garbage Collector (GC)**, ou Coletor de Lixo, roda periodicamente. Ele "caça" os objetos na memória que não estão mais sendo referenciados por nenhuma parte do programa e libera o espaço ocupado por eles.
* **A consequência:** O risco de erros de memória, como os vazamentos, é drasticamente reduzido. O programador produz código mais rápido e seguro. A desvantagem é a perda de controle e uma pequena sobrecarga de desempenho, pois o GC consome tempo de processamento e pode causar pequenas pausas na execução do programa.


 ```c 
  int* ptr; 
  ptr = (int*) malloc(10 * sizeof(int)); /* ... uso da memória ... */ 
  free(ptr); // Obrigatório! 
  // 
  ``` 

  ```java 
  public void meuMetodo() { ArrayList<String> lista = new ArrayList<>(); /* ... uso da lista ... */ // A memória será liberada pelo GC. } ``` 
