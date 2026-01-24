## Se quisermos determinar se uma tupla tem um valor fixo, podemos usar a função hash, para criar uma função fixed.

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])

print(fixed(tf))
print(fixed(tm))