#include <stdio.h>

int main(void)
{
    int i, numero, maior=0, posicao=0;


    for(i=1; i<=100; i++){
        scanf("%d", &numero);
        if(numero>maior){
            maior = numero;
            posicao = i;
        }
    }
    printf("%d\n%\n", maior, posicao);

    return 0;
}
