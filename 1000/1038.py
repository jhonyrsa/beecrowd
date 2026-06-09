cod_item, qde_item = map(int, input().split())
valor_total = 0.0

if cod_item == 1:
    valor_total = qde_item * 4.00
elif cod_item ==2:
    valor_total = qde_item * 4.50
elif cod_item == 3:
    valor_total = qde_item * 5.00
elif cod_item == 4:
    valor_total = qde_item * 2.00
elif cod_item == 5:
    valor_total = qde_item * 1.50

print(f"Total: R$ {valor_total :.2f}")