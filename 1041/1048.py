salario_atual = float(input())
salario_novo = 0.0
reajuste = 0.0
percentual = 0

if salario_atual <= 400.00:
    salario_novo = salario_atual * 1.15
    reajuste = salario_novo - salario_atual
    percentual = 15

elif salario_atual <= 800.00:
    salario_novo = salario_atual * 1.12
    reajuste = salario_novo - salario_atual
    percentual = 12

elif salario_atual <= 1200.00:
    salario_novo = salario_atual * 1.10
    reajuste = salario_novo - salario_atual
    percentual = 10

elif salario_atual <= 2000.00:
    salario_novo = salario_atual * 1.07
    reajuste = salario_novo - salario_atual
    percentual = 7

else:
    salario_novo = salario_atual * 1.04
    reajuste = salario_novo - salario_atual
    percentual = 4

print(f'Novo salario: {salario_novo:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')

