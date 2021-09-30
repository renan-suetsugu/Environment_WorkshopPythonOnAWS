# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Informe a distância que será percorrida: "))
velocidade = float(input("Informe a velocidade média esperada: "))

tempo_medio = distancia / velocidade

print(f"O tempo esperado de viagem é de: {tempo_medio} hora(s)")