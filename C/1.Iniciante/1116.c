#include <stdio.h>

int main(void)
{
    int i, N, X, Y;
    scanf("%d", &N);
    for(i=1; i<=N; i++){
        scanf("%d %d", &X, &Y);
        if(Y==0)
            printf("divisao impossivel\n");
        else
            printf("%.1f\n", (float)X/Y);
    }
    return 0;
}
