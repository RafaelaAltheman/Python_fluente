charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(lewis), id(charles))



alex = {'name': 'Charles L. Dodgson', 'born': 1832} 
print(alex == charles)
print(alex is not charles)

# alex é uma referência a um objeto que é uma réplica do objeto vinculado a charles.
#  Mas são objetos distintos. 