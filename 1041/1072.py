n = int(input())

dentro_intervalo = 0
fora_intervalo = 0

for i in range(n):
    numero = int(input())
    if numero >= 10 and numero <=20:
        dentro_intervalo +=1
    else:
        fora_intervalo +=1

print(f'{dentro_intervalo} in')
print(f'{fora_intervalo} out')
