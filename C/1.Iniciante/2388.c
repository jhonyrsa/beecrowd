#include <stdio.h>

int main(void)
{
    int i,N, resultado=0, T, V;

    scanf("%d", &N);

    for(i=1; i<=N; i++){
        scanf("%d %d", &T, &V);
        resultado = resultado + T*V;
    }
    printf("%d\n", resultado);

    return 0;
}
