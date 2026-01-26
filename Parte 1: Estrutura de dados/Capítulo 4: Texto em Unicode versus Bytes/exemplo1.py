# caracteres unicode

s = 'café' # tem 4 caracteres unicode
print(len(s))

b = s.encode('utf8')
print(b)
print(len(b))
print(b.decode('utf8'))