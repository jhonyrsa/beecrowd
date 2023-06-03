#include <stdio.h>

int main(void)
{
    int N;

    scanf("%d", &N);

    int X, Y,aux, soma =0;

    int i, j;

    for(i=1; i<=N; i++){
        scanf("%d %d",&X, &Y);
        if(X>Y){
            aux = X;
            X = Y;
            Y = aux;
        }
        for(j=X+1; j<Y; ++j){

            if(j%2!=0)
                soma = soma + j;
        }
        printf("%d\n", soma);
        soma=0;
    }
    return 0;
}
