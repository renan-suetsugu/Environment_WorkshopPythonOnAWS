# Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Informe o primeiro valor do cálculo: "))
num2 = float(input("Informe o segundo valor do cálculo: "))
operacao = input("Informa a operação (soma '+', subtação '-', multiplicação '*' ou divisão '/') que deseja realizar: ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    print("Operação informada não foi encontrada!")

print ("O resultado do cálculo é: %4.2f" % resultado) 