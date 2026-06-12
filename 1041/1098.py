jini = 1
jfim = 4
j = jini
i = 0
while i <= 2:
    j = jini
    if i == 0 or i == 1 or i == 2:
        while j < jfim:
            print(f'I={int(i)} J={int(j)}')
            j +=1
    else:
        while j < jfim:
            print(f'I={i:.1f} J={j:.1f}')
            j +=1
    jini = round(jini + 0.2, 1)
    jfim = round(jfim + 0.2, 1)
    i = round(i + 0.2, 1)
    