## EXPRESSÕES GERADORAS

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# aqui faz o produto cartesiano de uma genexp (expressao geradora)
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# a expressão geradora produz um item por vez, não cria uma lista 