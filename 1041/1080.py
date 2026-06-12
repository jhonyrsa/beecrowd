maior_numero = 0
posicao = 0

for i in range(1, 101):
    numero = int(input())
    if numero > maior_numero:
        maior_numero = numero
        posicao = i

print(maior_numero)
print(posicao)
