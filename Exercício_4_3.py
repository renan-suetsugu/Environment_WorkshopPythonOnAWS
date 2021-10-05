# Escreva um programa que leia três números e que imprima o maior e o menor.

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
num3 = float(input("Entre com o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número é o maior número: %6.2f" % num1)

if num2 > num1 and num2 > num3:
    print("O segundo número é o maior número: %6.2f" % num2)

if num3 > num1 and num3 > num2:
    print("O terceiro número é o maior número: %6.2f" % num3)

if num1 < num2 and num1 < num3:
    print("O primeiro número é o menor número: %6.2f" % num1)

if num2 < num1 and num2 < num3:
    print("O segundo número é o menor número: %6.2f" % num2)

if num3 < num1 and num3 < num2:
    print("O terceiro número é o menor número: %6.2f" % num3)