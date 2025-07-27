# Desafio 2: Ambientes de Programação

### 1. Compiladores

A abordagem de compilação consiste em uma tradução completa e antecipada. Um programa chamado **compilador** lê todo o código-fonte e o converte de uma só vez em um arquivo executável contendo código de máquina nativo.

-   **Vantagem Principal:** O desempenho é máximo, pois o programa final já está otimizado para o processador específico e não necessita de mais traduções durante a execução.
-   **Desvantagem Principal:** Perda de portabilidade. Um programa compilado para Windows não rodará em Linux, por exemplo. Além disso, qualquer alteração no código-fonte exige uma nova compilação completa.
-   **Exemplos de Linguagens:** C, C++, Rust.

### 2. Interpretadores

A abordagem de interpretação executa o código em tempo real, linha por linha. Um programa chamado **interpretador** lê uma instrução do código-fonte, a traduz para linguagem de máquina e a executa imediatamente, passando para a próxima.

-   **Vantagem Principal:** Alta portabilidade e flexibilidade. O mesmo código-fonte pode ser executado em qualquer sistema que possua o interpretador correto. O ciclo de desenvolvimento é rápido, pois não há etapa de compilação.
-   **Desvantagem Principal:** O desempenho é inferior ao de um código compilado, pois a tradução ocorre continuamente durante a execução.
-   **Exemplos de Linguagens:** Python (em modo interativo), Shell Script, JavaScript (historicamente).

### 3. Sistemas Híbridos e Máquinas Virtuais (VMs)

Esta abordagem combina o melhor dos dois mundos. O código-fonte é primeiro compilado para um código intermediário, de baixo nível, mas que não é nativo de nenhuma máquina. Esse código é chamado de **bytecode**. Em seguida, uma **Máquina Virtual (VM)** — um software que simula um processador — interpreta ou compila esse bytecode para o código de máquina nativo do sistema em que está rodando.

-   **Vantagem Principal:** Portabilidade total, resumida no lema "escreva uma vez, rode em qualquer lugar" (*write once, run anywhere*). O mesmo bytecode pode ser executado em qualquer plataforma que tenha a VM correspondente.
-   **Desvantagem Principal:** O desempenho pode ser ligeiramente inferior ao do código compilado nativamente, e a execução depende da presença da VM, que adiciona uma camada de abstração.
-   **Exemplos de Linguagens:** Java (com sua JVM), C# (com o .NET), Python (que gera arquivos `.pyc` contendo bytecode).

