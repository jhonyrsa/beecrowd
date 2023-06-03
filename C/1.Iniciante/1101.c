#include <stdio.h>

int main (void)
{
    int i,M, N, aux, soma=0;

    while(1){
        scanf("%d %d", &M, &N);

        if(M<=0 || N<=0) break;

        if(M>N){
            aux = N;
            N = M;
            M = aux;
        }

        for(i=M; i<=N; i++){
            printf("%d ", i);
            soma = soma+i;
        }

        printf("Sum=%d\n", soma);
        soma=0;
    }
    return 0;
}
