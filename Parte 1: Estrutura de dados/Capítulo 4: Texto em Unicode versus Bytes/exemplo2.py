
# bytes: criados a partir de uma str, dada uma certa codificação
cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])

# bytearray: 
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])