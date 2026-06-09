n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10.0

if media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')

else:
    if media >= 5.0 and media < 7.0:
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        exame = float(input())
        media = (media + exame) / 2
        print(f"Nota do exame: {exame:.1f}")
        if media >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {media:.1f}")
    else:
        print(f'Media: {media:.1f}')
        print("Aluno aprovado.")