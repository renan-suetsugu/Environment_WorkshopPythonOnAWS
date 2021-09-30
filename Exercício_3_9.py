# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos.

SEGUNDOS_EM_MINUTOS = 60
MINUTOS_EM_HORAS = 60 
HORAS_EM_DIAS = 24 

dias = int(input("Entre com a quantidade de dias a serem convertidos: "))
horas = int(input("Entre com a quantidade de horas a serem convertidas: "))
minutos = int(input("Entre com a quantidade de minutos a serem convertidos:"))
segundos = int(input("Entre com a quantidade de segundos a serem convetidos: "))

segundos_convertidos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print("O valor convertido em segundos é: ", segundos_convertidos)