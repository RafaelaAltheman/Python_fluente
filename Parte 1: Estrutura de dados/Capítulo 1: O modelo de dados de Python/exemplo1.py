# Um baralho como uma sequência de cartas
import collections

Card = collections.namedtuple('Card', ['rank', 'suit']) # representar uma classe simples representando cartas individuais
# namedtuple cria classes de objetos que são apenas um agrupamento de atributos, sem métodos prórpios, como um banco de dados

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
# função len retorna o número de cartas no baralho
deck = FrenchDeck()
print(len(deck))

# podemos acessar cartas individuais usando index (__getitem__)
print(deck[10])
print(deck[40])

#sorteio aleatório de cartas
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

# fatiamento também funciona
print(deck[:3]) #pega as 3 primeiras cartas do baralho (deck[0:3])
print(deck[12::13]) #início 12 e fim até o final, pulando de 13 em 13

#como temos o getitem o baralho é um objeto iterável, que pode ser usado em loops for
for card in deck:
    print(card)

#iterar com for de forma inversa 
# for card in reversed(deck):
#     print(card) 
    

#verificar se uma carta específica está no baralho
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

#ordenar cartas pelo valor numérico e depois naipes
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)