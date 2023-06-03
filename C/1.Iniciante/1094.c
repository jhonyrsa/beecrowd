#include <stdio.h>

int main(void)
{
    int i, N, amostra, coelho=0, rato=0, sapo=0, total=0;
    char Tipo;

    scanf("%d", &N);

    for(i=1; i<=N; i++){
        scanf("%d %c",&amostra, &Tipo);
        switch(Tipo){
            case 'C':
                coelho = coelho+amostra;
                total = total+amostra;
                break;
            case 'R':
                rato = rato+amostra;
                total = total+amostra;
                break;
            case 'S':
                sapo = sapo+amostra;
                total = total+amostra;
                break;
        }
    }
    printf("Total: %d cobaias\n", total);
    printf("Total de coelhos: %d\n", coelho);
    printf("Total de ratos: %d\n", rato);
    printf("Total de sapos: %d\n", sapo);
    printf("Percentual de coelhos: %.2f %%\n", (((float)coelho)/total)*100);
    printf("Percentual de ratos: %.2f %%\n", (((float)rato)/total)*100);
    printf("Percentual de sapos: %.2f %%\n", (((float)sapo)/total)*100);

    return 0;
}
