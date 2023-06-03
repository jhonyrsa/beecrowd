#include <stdio.h>

int calcFatorial(int A);

int main(void){

    int numero;

    scanf("%d", &numero);

    numero = calcFatorial(numero);

    printf("%d\n", numero);

    return 0;
}

int calcFatorial(int A){

    int i, result=1;

    for(i=1; i<=A; i++) result = result*i;

    return result;
}

