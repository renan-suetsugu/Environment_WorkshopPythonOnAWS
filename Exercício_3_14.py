# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

VALOR_KM_RODADO = 0.15
VALOR_DIARIA = 60

km_rodados = float(input("Entre com a quantidade de km rodados: "))
dias_locados = float(input("informe a quantidade de dias de locação: "))

preco_km = km_rodados * VALOR_KM_RODADO
preco_locacao = dias_locados * VALOR_DIARIA
preco_total = preco_km + preco_locacao

print(f"O valor da kilometragem rodada é de R${preco_km:.2f} e o valor da locação é R${preco_locacao:.2f}, totalizando R${preco_total:.2f}." )