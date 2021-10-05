# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa_valor = float(input("Informe o valor da casa que deseja comprar: "))
salário = float(input("Informe o valor do salário: "))
anos_pagamento = int(input("Informe a quantidade de anos que irá pagar: "))

prestação = casa_valor / (anos_pagamento * 12)
trinta_porcento_salario = salário * 0.3

if prestação <= trinta_porcento_salario:
    print ("O valor das prestações do imóvel é: R$%5.2f" % prestação)
else:
    print ("O valor da prestação no pode ser superior à 30 porcento do salário.")
