hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
duracao_min = 0
duracao_horas = 0
if hora_inicial < hora_final:
    duracao_min = (hora_final - hora_inicial) * 60 - minuto_inicial + minuto_final
    duracao_horas = duracao_min // 60
    duracao_min = duracao_min % 60
elif hora_final < hora_inicial:
    duracao_min = (24 - hora_inicial + hora_final) * 60 - minuto_inicial + minuto_final
    duracao_horas = duracao_min // 60
    duracao_min = duracao_min % 60
else:
    if minuto_inicial < minuto_final:
        duracao_min = minuto_final - minuto_inicial
        duracao_horas = 0
        
    elif minuto_inicial > minuto_final:
        duracao_min = (24 * 60) - minuto_inicial + minuto_final
        duracao_horas = duracao_min // 60
        duracao_min = duracao_min % 60
        
    else: 
        duracao_min = 0
        duracao_horas = 24

print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_min} MINUTO(S)')