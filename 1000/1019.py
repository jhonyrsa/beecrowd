tempo_total_segundos = int(input())

tempo_horas = tempo_total_segundos // 3600
tempo_minutos = (tempo_total_segundos % 3600) // 60
tempo_segundos = ((tempo_total_segundos % 3600) % 60)

print(f'{tempo_horas}:{tempo_minutos}:{tempo_segundos}')
