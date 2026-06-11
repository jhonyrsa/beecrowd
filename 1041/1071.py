x = int(input())
y = int(input())

abs_x = abs(x)
abs_y = abs(y)

diferenca = 0
menor = 0
maior = 0
soma = 0

if abs_x > abs_y:
    diferenca = abs_x - abs_y
    menor = y
    maior = x
elif abs_x < abs_y:
    diferenca = abs_y - abs_x
    menor = x
    maior = y

for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma = soma + i

print(soma)