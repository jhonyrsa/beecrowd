x = int(input())
y = int(input())

x_trocado = min(x, y)
y_trocado = max(x, y) + 1

soma_nao_multiplos_treze = 0

for i in range(x_trocado, y_trocado):

    if i % 13 != 0:
        soma_nao_multiplos_treze += i

print(soma_nao_multiplos_treze)
