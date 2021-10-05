# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

# Preço por tipo e faixa de consumo
# Tipo Faixa    (kWh)           Preço

# Residencial   Até 500         R$ 0,40
#               Acima de 500    R$ 0,65

# Comercial     Até 1000        R$ 0,55
#               Acima de 1000   R$ 0,60

# Industrial    Até 5000        R$ 0,55
#               Acima de 5000   R$ 0,60

kilowatts_hora = int(input("Informe o consumo de kWh: "))
tipo_instalação = input("Informe o tipo de instação. (Ex.: R para residências, I para indústrias e C para comércios.): ")

if tipo_instalação == 'R':
    if kilowatts_hora <= 500:
        valor_fatura = kilowatts_hora * 0.40
    else:
        valor_fatura = kilowatts_hora * 0.65
elif tipo_instalação == 'C':
    if kilowatts_hora <= 1000:
        valor_fatura = kilowatts_hora * 0.55
    else:
        valor_fatura = kilowatts_hora * 0.60
elif tipo_instalação =='I':
    if kilowatts_hora <= 5000:
        valor_fatura = kilowatts_hora * 0.55
    else:
        valor_fatura = kilowatts_hora * 0.60
else:
    print ("O tipo de instalação informado está incorreto!")

print ("O valor da fatura de é: R$%6.2f." % valor_fatura)