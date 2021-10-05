# Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

km_percorrido = float(input("Informe o km que será percorrido: "))

if km_percorrido <= 200:
    preco_passagem = km_percorrido * 0.50
    print ("O preço da passagem de acordo com a km é de: R$%4.2f" % preco_passagem)
else:
    preco_passagem = km_percorrido * 0.45
    print ("O preço da passagem de acordo com a km é de: R$%4.2f" % preco_passagem)