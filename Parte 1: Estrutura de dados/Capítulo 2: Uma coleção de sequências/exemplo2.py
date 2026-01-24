## lISTAS DE COMPREENSÃO

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes] #listcomp
#tshirts = [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),('white', 'M'), ('white', 'L')]

for color in colors:  
    for size in sizes:
        print((color, size))

    #loops for estao aninhados na mesma ordem que aparecem na listcomp