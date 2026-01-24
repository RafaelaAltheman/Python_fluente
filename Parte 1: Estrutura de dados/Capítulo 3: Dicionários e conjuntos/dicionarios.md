# Dicionários e conjuntos

### Usamos dicionários em todos os nossos programas Python. Se não diretamente em nosso código, então indiretamente, pois o tipo dict é um elemento fundamental da implementação de Python.

# Método get_creators()

### recebe um dicionário e retorna uma lista

# Hashble

### Um objeto é hashable se tem um código de hash que nunca muda durante seu ciclo de vida (precisa ter um método __hash__) e pode ser comparado com outros objetos (precisa ter um método __eq__). Objetos hashable que são comparados como iguais devem ter o mesmo código de hash.

# Defaultdict

### é um tipo de dicionário especial do módulo collections que cria automaticamente um valor padrão quando você acessa uma chave que ainda não existe.

# método __missing__

### é um método especial de dicionários que é chamado automaticamente quando você acessa uma chave inexistente 

# collection.ChainMap

### lista de mapeamentos de ChainMap mantém uma lista de mapeamentos que podem ser consultados como se fossem um mapeamento único. 

# collection.Counter

### é uma subclasse de dict feita para contar elementos hashable automaticamente.

# shelve.Shelf

### fornecxe armazenamento persistente a um mapeamento de chaves em formato string para objetos python

# Operações básicas do dicionário:

### d.keys() --> view das chaves do dict
### d.values() --> view de cada um dos elementos do dict 
### d.items() --> view que retorna os pares (key, value)

