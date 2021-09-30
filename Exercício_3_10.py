# Exercício 3.10 Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

salario = float(input("Informe o salário atual: "))
porcentagem_aumento = float(input("Informe a porcentagem de correção salarial: "))

aumento = salario * porcentagem_aumento / 100
novo_salario = salario + aumento

print (f"O valor do aumento é: {aumento}, E o novo salário é: {novo_salario}")