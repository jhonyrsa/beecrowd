x = int(input())
y = int(input())

x_trocado = min(x, y) + 1
y_trocado = max(x, y)

for i in range(x_trocado, y_trocado):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
