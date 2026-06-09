valor_lido = int(input())
print(f'{valor_lido}')

nota_cem = valor_lido // 100
print(f'{nota_cem} nota(s) de R$ 100,00')

nota_cinquenta = (valor_lido % 100) // 50
print(f'{nota_cinquenta} nota(s) de R$ 50,00')

nota_vinte = ((valor_lido % 100) % 50) // 20
print(f'{nota_vinte} nota(s) de R$ 20,00')

nota_dez = (((valor_lido % 100) % 50) % 20) // 10
print(f'{nota_dez} nota(s) de R$ 10,00')

nota_cinco = ((((valor_lido % 100) % 50) % 20) % 10) // 5
print(f'{nota_cinco} nota(s) de R$ 5,00')

nota_dois = (((((valor_lido % 100) % 50) % 20) % 10) % 5) // 2
print(f'{nota_dois} nota(s) de R$ 2,00')

nota_um = (((((valor_lido % 100) % 50) % 20) % 10) % 5) % 2
print(f'{nota_um} nota(s) de R$ 1,00')
