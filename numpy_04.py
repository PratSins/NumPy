# NumPy Mathematics

import numpy as np

a = np.array([1, 2,3, 4])
print("a - ",a)
print()

a = a + 2
print("a - ",a)
a = a - 2
print("a - ",a)
a = a * 2
print("a - ",a)
a = a ** 2
print("a - ",a)
a = a / 2
print("a - ",a)
print()

b = np.array([1,0,1,0])
print("b - ",b)
k = a + b
print("k - ",k)
k = a * b
print("k - ",k)
print()

c = np.sin(b)
print("c - ",c)
c = np.cos(b)
print("c - ",c)
print()