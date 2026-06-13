qde_entradas = int(input())

for i in range(qde_entradas):
    x, y = map(int, input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print(f'{divisao:.1f}')
        