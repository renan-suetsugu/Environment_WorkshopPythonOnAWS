# Listagem 4.6 – Conta de telefone com três faixas de preço
# Vejamos o exemplo de calcular a conta de um telefone celular da empresa Tchau.

# Os planos da empresa Tchau são bem interessantes e oferecem preços diferenciados de acordo com a quantidade de minutos usados por mês. 
# Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
# Entre 200 e 400 minutos, o preço é de R$ 0,18. Acima de 400 minutos, o preço por minuto é de R$ 0,15.
# O programa da listagem 4.6 resolve esse problema.

minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else: 
        preço = 0.15 

print("Você vai pagar este mês: R$%6.2f" % (minutos * preço))