t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]), id(t2[-1]))
t1[-1].append(99)
print(t1)


l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)