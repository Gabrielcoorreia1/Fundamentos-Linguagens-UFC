# Desafio 3: Descrições Sintáticas e Semânticas

## Apresentando a Linguagem "Astro"

Para ilustrar os conceitos, foi inventada uma mini-linguagem de domínio específico chamada **Astro**. Seu propósito é puramente declarativo: descrever corpos celestes e suas propriedades básicas, como tipo e massa. A sintaxe foi projetada para ser simples e legível, similar a formatos de configuração como JSON.

## Definição da Gramática Fictícia

A estrutura de uma linguagem é formalmente descrita por uma **gramática**. A seguir, a gramática da linguagem Astro é apresentada usando uma notação similar à BNF (*Backus-Naur Form*), que utiliza um conjunto de regras de derivação para definir a sintaxe.

```
<programa> ::= <declaracao_astro> | <programa> <declaracao_astro>
<declaracao_astro> ::= 'astro' <id> '{' <lista_props> '}'
<lista_props> ::= <propriedade> | <lista_props> ',' <propriedade>
<propriedade> ::= <tipo_prop> ':' <valor>
<tipo_prop> ::= 'tipo' | 'massa' | 'orbita'
<valor> ::= <string> | <numero> | <id>
<id> ::= letra (letra | digito)*
<numero> ::= digito+ ('.' digito+)?
<string> ::= '"' (qualquer caractere exceto '"')* '"'
```
* `<programa>`: Um programa em Astro é uma sequência de uma ou mais declarações de astros.
* `<declaracao_astro>`: Cada astro é definido pela palavra-chave `astro`, um nome (`id`) e um bloco de propriedades entre chaves `{}`.
* `<propriedade>`: Uma propriedade consiste em um nome, dois-pontos e um valor.

## Exemplo de Análise Léxica: De Código a Tokens

A primeira fase da interpretação de um código é a **análise léxica**. Nela, um programa chamado *lexer* (ou *scanner*) varre o texto do código-fonte e o quebra em uma sequência de unidades atômicas chamadas **tokens**. Cada token representa um elemento indivisível da linguagem (como uma palavra-chave, um identificador ou um operador).

Abaixo, vemos um exemplo de código em Astro e a sequência de tokens gerada por um analisador léxico.

**Código-fonte em Astro:**

```astro
astro Sol {
  tipo: "Estrela",
  massa: 1.989
}
```

**Resultado da Análise Léxica (Sequência de Tokens):**

| Lexema (O que foi lido) | Token (O que significa) |
| :--- | :--- |
| `astro` | PALAVRA_CHAVE_ASTRO |
| `Sol` | IDENTIFICADOR |
| `{` | ABRE_CHAVE |
| `tipo` | IDENTIFICADOR |
| `:` | DOIS_PONTOS |
| `"Estrela"` | LITERAL_STRING |
| `,` | VIRGULA |
| `massa` | IDENTIFICADOR |
| `:` | DOIS_PONTOS |
| `1.989` | LITERAL_NUMERICO |
| `}` | FECHA_CHAVE |