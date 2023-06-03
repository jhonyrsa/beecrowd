#include <stdio.h>

int main(void)
{
    float nota1, nota2;

    Nota1:
    scanf("%f", &nota1);
    if(nota1<0 || nota1>10.0){
        printf("nota invalida\n");
        goto Nota1;
    }

    Nota2:
    scanf("%f", &nota2);
    if(nota2<0 || nota2>10.0){
        printf("nota invalida\n");
        goto Nota2;
    }
    printf("media = %.2f\n", (nota1+nota2)/2);
    return 0;
}
