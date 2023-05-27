import numpy as np

k = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25],
     [26,27,28,29,30],]

a = np.array(k)
print("a -\n",a)
print()

b = a[2:4, 0:2]
print("b -\n",b)
print()

c = a[ [0,1,2,3], [1,2,3,4] ]
print("c - ",c)
print()

d = a[[0,4,5], 3:]
print("d -\n",d)
print()