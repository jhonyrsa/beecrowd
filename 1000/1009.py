nome_vendedor = input()
salario_fixo = float(input())
total_vendas_mes = float(input())
COMISSAO = 0.15

salario_com_bonus = salario_fixo + total_vendas_mes * COMISSAO

print(f'TOTAL = R$ {salario_com_bonus:.2f}')