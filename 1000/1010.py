entrada1 = input().split()
cod_peca1 = int(entrada1[0])
qde_peca1 = int(entrada1[1])
valor_unitario_peca1 = float(entrada1[2])

entrada2 = input().split()
cod_peca2 = int(entrada2[0])
qde_peca2 = int(entrada2[1])
valor_unitario_peca2 = float(entrada2[2])

valor_a_pagar = (qde_peca1 * valor_unitario_peca1) + (qde_peca2 * valor_unitario_peca2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_a_pagar))
