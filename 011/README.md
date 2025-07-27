# Desafio 11: Programação Funcional

## O Problema: Análise de Notas de Alunos

Imaginei um cenário simples: tenho uma lista de alunos, cada um com seu nome e uma lista de notas. O meu objetivo é calcular a **média final apenas dos alunos aprovados**, considerando que para ser aprovado, a média do aluno precisa ser igual ou superior a 7.0.

Este problema é ótimo para a abordagem funcional porque envolve uma série de transformações e filtros sobre um conjunto de dados.

## A Solução Funcional: Um Pipeline de Dados

Em vez de usar laços `for` e variáveis que mudam de valor (estilo imperativo), a abordagem funcional enxerga a solução como um "pipeline" por onde os dados fluem e são transformados em etapas.

1.  **Mapear para calcular a média de cada aluno:** A primeira etapa é transformar nossa lista de alunos em uma lista que também contenha a média de cada um. Usei a função de alta ordem `map()` para aplicar uma função de cálculo de média a cada aluno da lista.

2.  **Filtrar os alunos aprovados:** Com as médias calculadas, o próximo passo é filtrar essa lista, mantendo apenas os alunos com média >= 7.0. A função `filter()` é perfeita para isso, pois ela "peneira" a lista com base em uma condição.

3.  **Mapear para extrair as médias finais:** Agora que temos apenas os alunos aprovados, não nos importamos mais com seus nomes, apenas com suas médias. Usei `map()` novamente para extrair apenas as notas médias, transformando nossa lista de objetos em uma simples lista de números.

4.  **Reduzir para calcular a média final:** O último passo é pegar essa lista de médias e calcular a média geral. Para demonstrar a **recursão**, criei uma função `soma_recursiva` que soma os elementos da lista. O cálculo final da média usa essa soma.

## Código-Fonte da Solução

O código-fonte completo, escrito em Python, está no arquivo `processador_dados.py`. Ele implementa todo o pipeline de dados descrito acima.

Para executar e ver a análise em ação:
```bash
python processador_dados.py
```