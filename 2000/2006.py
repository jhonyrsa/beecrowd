tipo_cha = int(input())

aposta = input().split()

chutes_certos = 0

for i in range (5):
    aposta_i = int(aposta[i])
    if aposta_i == tipo_cha:
        chutes_certos += 1

print(chutes_certos)
    