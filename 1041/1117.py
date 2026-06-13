soma = 0
media = 0
i = 0
while True:
    x = float(input())

    if x < 0 or x > 10:
        print('nota invalida')

    elif 0 <= x <=10:
        soma += x
        i += 1

    if i == 2:
        break

media = soma / i
print(f'media = {media:.2f}')