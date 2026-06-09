valor_lido = float(input())

# Multiplicamos por 100 e usamos o round() antes do int() 
# para garantir que não haja perda na conversão do float.
valor = int(round(valor_lido * 100))

# NOTAS (valores em centavos: 100 reais = 10000 centavos)
nota_cem = valor // 10000
valor %= 10000 # Isso é o mesmo que: valor = valor % 10000

nota_cinquenta = valor // 5000
valor %= 5000

nota_vinte = valor // 2000
valor %= 2000

nota_dez = valor // 1000
valor %= 1000

nota_cinco = valor // 500
valor %= 500

nota_dois = valor // 200
valor %= 200

# MOEDAS (valores em centavos)
moeda_um = valor // 100
valor %= 100

moeda_cinquenta = valor // 50
valor %= 50

moeda_vinte_cinco = valor // 25
valor %= 25

moeda_dez = valor // 10
valor %= 10

moeda_cinco = valor // 5
valor %= 5

# O que sobrar são as moedas de 1 centavo
moeda_um_centavo = valor // 1

print('NOTAS:')
print(f'{nota_cem} nota(s) de R$ 100.00')
print(f'{nota_cinquenta} nota(s) de R$ 50.00')
print(f'{nota_vinte} nota(s) de R$ 20.00')
print(f'{nota_dez} nota(s) de R$ 10.00')
print(f'{nota_cinco} nota(s) de R$ 5.00')
print(f'{nota_dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda_um} moeda(s) de R$ 1.00')
print(f'{moeda_cinquenta} moeda(s) de R$ 0.50')
print(f'{moeda_vinte_cinco} moeda(s) de R$ 0.25')
print(f'{moeda_dez} moeda(s) de R$ 0.10')
print(f'{moeda_cinco} moeda(s) de R$ 0.05')
print(f'{moeda_um_centavo} moeda(s) de R$ 0.01')
