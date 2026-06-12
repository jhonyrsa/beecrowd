numero_casos = int(input())
soma_impares = 0

while numero_casos >= 1:
    entrada1, entrada2 = map(int, input().split())
    x = min(entrada1, entrada2)
    y = max(entrada1, entrada2)
    soma_impares = 0

    while x < y:
        x +=1
        if x == y:
            break
        elif x % 2 != 0:
            soma_impares += x
    print(soma_impares)
    numero_casos -=1