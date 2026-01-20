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
