city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))

#UNicodedecodeerror

octets = b'Montr\xe9al' 
octets.decode('cp1252')
print(octets.decode('utf_8'))  