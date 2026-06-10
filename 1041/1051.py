salario = float(input())
diferenca = 0.00
imposto = 0.00

if salario > 4500.00:
    diferenca = salario - 4500.00
    #print(f'{diferenca:.2f}')

    imposto = diferenca * 0.28
    #print(f'{imposto:.2f}')

    salario = salario - diferenca
    #print(f'{salario:.2f}')

#print(f'{salario:.2f}')

if salario > 3000.00 and salario <= 4500.00:
    diferenca = salario - 3000.00
    #print(f'{diferenca:.2f}')

    imposto = imposto + diferenca * 0.18
    #print(f'{imposto:.2f}')

    salario = salario - diferenca
    #print(f'{salario:.2f}')

#print(f'{salario:.2f}')

if salario > 2000.00 and salario <= 3000.00:
    diferenca = salario - 2000.00
    #print(f'{diferenca:.2f}')

    imposto = imposto + diferenca * 0.08
    #print(f'{imposto:.2f}')

    salario = salario - diferenca
    #print(f'{salario:.2f}')

#print(f'{salario:.2f}')

if imposto == 0.00:
    print('Isento')
else:
    print(f'R$ {imposto:.2f}')