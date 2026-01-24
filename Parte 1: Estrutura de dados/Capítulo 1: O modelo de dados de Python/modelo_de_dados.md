# Modelo de Dados de Python

# Métodos __getitem__ e __len__

# 1. collections.namedtuple

## Cria uma classe simples, usada para agrupar dados sem comportamento, como linhas de banco de dados 

### Card = collections.namedtuple('Card', ['rank', 'suit'])

# 2. Método __len__

## Permite contar os elementos de uma lista

### def __len__(self): return len(self._cards)

# 2. Método __getitem__

## Acessar elementos pelo indice

## slicing: extrai subconjuntos de uma sequência ([início : fim : passo])

### início: indice que começa, fim: indice que termina, passo: de quantos em quantos elementos o indice avança

## iteração (for): o objeto de torna iterávek, pois o getitem é usado sequencialmente

## iteração reversa: reversed()

# 3. Operador in: funciona porque o objeto é iterável

# 4. Random choice: retorna um elemento aleatório de uma sequência 

# 5. sorted() + key

## sorted: aceita qualquer objeto iterável
## key: define o critério de ordenação

### sorted(deck, key=spades_high)

# 6. __init__ 

## Inicializa o objeto

# 7. __repr__

## Define como objeto aparece no terminal, formato string

# 8. __abs__

## apresenta o módulo do vetor

# 9. __bool__

## Define o valor lógico do objeto, se for um vetor nulo (False) e Vetor com valor(True)

# 10. __add__

## Define o operador + 

# 11. __mul__ 

## Multiplicação escalar, retorna novo vetor que tenha a mesma direção

