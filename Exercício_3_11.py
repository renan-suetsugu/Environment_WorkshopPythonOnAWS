# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input("Entre com o valor da mercadoria: "))
percentual = float(input("Entre com o percentual de desconto: "))

desconto = mercadoria * percentual / 100
preco_a_pagar = mercadoria - desconto

print (f"O valor do desconto é de R${desconto} e o preço a ser pago é de R${preco_a_pagar}")