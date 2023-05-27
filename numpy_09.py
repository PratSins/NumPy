# Boolean Masking

import numpy as np

k = [ [  1,  13,  21,  11, 196,  75,   4,   3,  34,   6,   7,   8,   0,   1,   2,   3,   4,   5],
      [  3,  42,  12,  33, 766,  75,   4,  55,   6,   4,   3,   4,   5,   6,   7,   0,  11,  12],
      [  1,  22,  33,  11, 999,  11,   2,   1,  78,   0,   1,   2,   9,   8,   7,   1,  76,  88]]

a = np.array(k)
print("a -\n",a)
print()

k1 = a > 50

print("a > 50   --->\n",k1)

k2 = a[a > 50]
print("\na[a > 50]   --->\n",k2)
print()

k3 = np.any(a > 50, axis=0)
print("np.any(a > 50, axis=0)  --->  ",k3)
print()

k4 = np.all(a > 50, axis=0)
print("np.all(a > 50, axis=0)  --->  ",k4)
k4 = np.all(a > 50, axis=1)
print("np.all(a > 50, axis=1)  --->  ",k4)
print()

k5 = ((a > 50) & (a <100))
print("((a > 50) & (a <100))   --->  ",k5)
k5 = (~((a > 50) & (a <100)))
print("\n(~((a > 50) & (a <100)))   --->  ",k5)
print()


print("\n---You can index with a List in NumPY---")
a = np.array([1,2,3,4,5,6,7,8,9])
print("a - ",a)
print(">> a[[1,2,8]] - ",a[[1,2,8]])