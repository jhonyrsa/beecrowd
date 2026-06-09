a, b, c = map(int, input().split())

maior_ab = (a + b + abs(a - b)) / 2
maior_ab = int(maior_ab)

#print(maior_ab)

maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2
maior_abc = int(maior_abc)

#print(maior_abc)

print(f'{maior_abc} eh o maior')
