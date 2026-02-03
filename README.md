# Python Fluente — Capítulos 1 a 6


## Capítulo 1 — Modelo de Dados do Python

O modelo de dados do Python é o conjunto de regras para definir como os objetos vão se comportar.

Python não é orientado por tipo fixo, ou seja importa o que o objeto faz, não o que ele é.                        
Objetos se integram ao ecossistema da linguagem ao implementar métodos especiais como:

- `__len__`: retorna o tamanho de um objeto.
- `__getitem__`: Método que define como acessar um elemento de um objeto usando colchetes.
- `__iter__`: Método que retorna um iterador.
- `__repr__`: Define como o objeto aparece quando você imprime.

Funções embutidas (`len`, `sorted`, `sum`) e operadores (`in`, `[]`) não verificam o tipo do objeto, mas sim se ele suporta determinado comportamento.  

Ideia principal: implementar poucos métodos especiais já permite que um objeto se comporte como tipo do Python.

---

## Capítulo 2 — Sequências

Python possui vários tipos de sequência: list, tuple, str, range...
Ao implementar apenas `__getitem__`, um objeto já pode:

- ser iterado (for)
- suportar slicing (:)
- funcionar com o operador `in`: Operador que verifica se um elemento pertence a uma coleção.

Mutáveis: podem ser alteradas no lugar (list)
Imutáveis: não mudam depois de criadas (tuple)

Isso demonstra como o Python reutiliza comportamentos existentes sem exigir herança explícita de classes.  
Muitas funcionalidades surgem automaticamente a partir de poucos métodos bem definidos.

Ideia principal: o Python favorece reutilização de comportamento por meio de protocolos, não hierarquias complexas.

---

## Capítulo 3 — Dicionários e Conjuntos

O `dict` é a estrutura de dados central do Python.  
Seu funcionamento depende de hashing, o que impõe regras importantes:

- chaves devem ser imutáveis, porque dependem de um hash que não pode mudar
- `__hash__` deve ser consistente com `__eq__`

hashing: transforma um objeto em um valor numérico fixo, para localizar valores em dict.

O capítulo também explora os conjuntos (`set`).

Mais do que estruturas de armazenamento, dicionários e conjuntos comunicam no código.

Usos: 
- list: coleção ordenada e mutável
- tuple: coleção ordenada e imutável
- set: coleções de elementos únicos, que também tem super metódos, lista de elementos únicos
- dict: associação chave --> valor

Ideia principal: `dict` e `set` são ferramentas conceituais, não apenas coleções de dados.

---

## Capítulo 4 — Texto vs Bytes (Unicode)

- `str` (texto Unicode)
- `bytes` (dados binários)
- ASCII

Unicode define os caracteres; UTF-8 define como esses caracteres são representados em bytes.  
Problemas surgem quando dados são codificados ou decodificados incorretamente.

O livro apresenta o conceito do sanduíche de Unicode:

- decodificar bytes para `str` assim que os dados entram
- processar internamente apenas texto Unicode
- codificar para bytes apenas na saída

Também é discutida a normalização Unicode, necessária para comparar strings visualmente idênticas mas binariamente diferentes.

Diferença str e bytes: 
- str: texto unicode
- bytes: dados binários

Ideia principal: muitos bugs de string são causados por mistura errada de texto e bytes. Por isso, sempre decodificar bytes para string e só dar encode para bytes na saída.

---

## Capítulo 5 — Estruturas de Dados

O capítulo discute como diferentes estruturas expressam intenção no código:

- mutável vs imutável
- sequência vs mapeamento
- registro simples vs objeto 

São comparados tipos como `tuple`, `NamedTuple` e `dataclass`, mostrando que a escolha da estrutura afeta o código.

- tuple: Uma tuple é uma coleção ordenada e imutável. Usar para análises simples, em que a posição do elemento importa
- NamedTuple: Uma tuple com nomes para os campos. 
- dataClass: Versão moderna do namedtuple, com anotações de tipo. (padrão moderno para modelar os dados, tem métodos automáticos)

Ideia principal: escolher a estrutura correta é uma decisão importante, não apenas técnica.

---

## Capítulo 6 — Referências, Mutabilidade e Memória

- variáveis são referências a objetos, não caixas de valores
- objetos mutáveis podem ser compartilhados 

---

## Principais pontos

- Python é orientado a comportamento, não a herança rígida
- Muitos bugs vêm de:
  - mutabilidade não intencional
  - compartilhamento de estado
  - confusão entre texto e bytes


