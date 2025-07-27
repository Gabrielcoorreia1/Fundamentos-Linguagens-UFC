#include <stdio.h>


void modificar_por_valor(int a) {
    printf("  > Dentro da função (valor), 'a' valia %d. Agora vale 100.\n", a);
    a = 100;
}

void modificar_por_referencia(int *b) {
    printf("  > Dentro da função (ref), o valor em '*b' era %d. Agora é 200.\n", *b);
    *b = 200;
}

int main() {
    int numero_original = 10;
    printf("O número original antes de tudo vale: %d\n\n", numero_original);
    printf("1. Chamando por valor...\n");
    modificar_por_valor(numero_original);
    printf(" -> Após a chamada por valor, o número original ainda vale: %d\n\n", numero_original);
    printf("2. Chamando por referência...\n");
    modificar_por_referencia(&numero_original);
    printf(" -> Após a chamada por referência, o número original mudou para: %d\n", numero_original);

    return 0;
}