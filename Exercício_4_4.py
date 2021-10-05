# Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Entre com o salário: "))

if salario > 1250:
    novo_salario = salario + salario * 0.10

if salario <= 1250:
    novo_salario = salario + salario * 0.15

print("O salário reajustado é: R$%6.2f" % novo_salario)
