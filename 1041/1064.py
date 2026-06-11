qde = 0
soma_anteriores = 0.0
media = 0.0

for i in range(0, 6):
    num = float(input())
    
    if num > 0:
        qde = qde + 1
        soma_anteriores = soma_anteriores + num
        media = soma_anteriores / qde

print(f"{qde} valores positivos")
print(f"{media:.1f}")