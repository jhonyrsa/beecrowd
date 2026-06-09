tempo_gasto_viagem = int(input())
velocidade_carro = int(input())

distancia_percorrida = tempo_gasto_viagem * velocidade_carro

KM_POR_LITRO = 12

quantidade_combustivel = distancia_percorrida / KM_POR_LITRO

print(f'{quantidade_combustivel:.3f}')
