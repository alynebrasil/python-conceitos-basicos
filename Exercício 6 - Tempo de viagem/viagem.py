# distância da viagem em quilômetros
distancia = 700
#distancia = int(input('Digite a distância em quilômetros: '))
# velocidade dos meios de transporte em km/h
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# calcular o tempo por cada transporte e exibir os tempos de viagem diretamente na impressão
print(f"Tempo de viagem de avião: {distancia / velocidade_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {distancia/ velocidade_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {distancia / velocidade_onibus:.2f} horas")