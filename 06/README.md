# Desafio 6: Subprogramas e Passagem de Parâmetros

### C: Controle Explícito com Ponteiros

Em C, a escolha entre valor e referência é totalmente manual e explícita. Você, como programador, precisa dizer exatamente o que quer fazer usando ponteiros (`*` para acessar o valor de um endereço e `&` para obter o endereço de uma variável).

O código completo que demonstra essa funcionalidade está na pasta `exemplo_c/`, no arquivo `main.c`.

Para compilar e executar o exemplo em um sistema com GCC:
```bash
gcc exemplo_c/main.c -o exemplo_c/executavel_c
./exemplo_c/executavel_c
```

### Python: A Nuance da "Passagem por Atribuição"

Python tem uma abordagem que não é puramente por valor nem por referência, mas sim "passagem por atribuição". O comportamento prático depende se o tipo de dado é **mutável** (como uma lista) ou **imutável** (como um número), o que pode parecer passagem por referência e por valor, respectivamente.

O código que ilustra este comportamento está na pasta `exemplo_python/`, no arquivo `main.py`.

Para executar o exemplo:
```bash
python exemplo_python/main.py
```
