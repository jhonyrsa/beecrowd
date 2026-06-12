numeros_caso_teste = int(input())

testes_coelho = 0
testes_sapo = 0
testes_rato = 0

testes_total = 0

for i in range(numeros_caso_teste):
    testes = input().split()
    numero_testes = int(testes[0])
    cobaia_teste = testes[1]

    if cobaia_teste == ('C'):
        testes_coelho += numero_testes
    elif cobaia_teste == ('R'):
        testes_rato += numero_testes
    elif cobaia_teste == ('S'):
        testes_sapo += numero_testes

    testes_total += numero_testes

print(f'Total: {testes_total} cobaias')
print(f'Total de coelhos: {testes_coelho}')
print(f'Total de ratos: {testes_rato}')
print(f'Total de sapos: {testes_sapo}')
print(f'Percentual de coelhos: {((testes_coelho / testes_total) * 100):.2f} %')
print(f'Percentual de ratos: {((testes_rato / testes_total) * 100):.2f} %')
print(f'Percentual de sapos: {((testes_sapo / testes_total) * 100):.2f} %')