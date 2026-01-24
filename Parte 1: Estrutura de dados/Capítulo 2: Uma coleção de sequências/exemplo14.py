# NUMPY

import numpy as np 
a = np.arange(12)  
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4 
print(a)
print(a.transpose())

# DEQUE

from collections import deque
dq = deque(range(10), maxlen=10) 
print(dq)
dq.rotate(3)
print(dq)