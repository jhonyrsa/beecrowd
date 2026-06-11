qde_pares = 0
qde_impares = 0
qde_positivos = 0
qde_negativos = 0

for i in range(0, 5):
    num = int(input())

    if num % 2 == 0:
        qde_pares += 1
    else:
        qde_impares += 1

    if num > 0:
        qde_positivos += 1
    elif num < 0:
        qde_negativos += 1

print(f'{qde_pares} valor(es) par(es)')
print(f'{qde_impares} valor(es) impar(es)')
print(f"{qde_positivos} valor(es) positivo(s)")
print(f"{qde_negativos} valor(es) negativo(s)")
