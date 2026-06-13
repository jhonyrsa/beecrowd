x, y = map(int, input().split())

while True:
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else:
        break

    x, y = map(int, input().split())