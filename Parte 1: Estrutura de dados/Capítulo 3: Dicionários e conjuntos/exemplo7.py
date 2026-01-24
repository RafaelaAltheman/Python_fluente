## Counter usado para contar letras na palavra

import collections


ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(3))