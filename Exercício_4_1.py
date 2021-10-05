# Analise o programa da listagem 4.2. Responda o que acontece se o primeiro e o segundo valores forem iguais? Explique.

# Resposta: O interpretador Python ignora as funções 2 e 4 e não retorna nenhuma informação, pois não existe nenhuma ação em caso de valores falsos.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    print ("O primeiro número é o maior!")
if b > a:
    print ("O segundo número é o maior!")