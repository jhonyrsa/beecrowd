soma = 0
i = 0
sel = 1
while sel == 1 or sel != 2:
    x = float(input())
    if x < 0 or x > 10:
        print('nota invalida')
    else:
        soma += x
        i +=1

    if i == 2:
        media = soma / i
        print(f'media = {media:.2f}')
        soma = 0
        while True:
            if i == 2:
                i = 0
                sel = int(input('novo calculo (1-sim 2-nao)\n'))
            if sel == 1 or sel == 2:
                break
            else:
                sel = int(input('novo calculo (1-sim 2-nao)\n'))
