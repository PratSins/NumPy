# NumPy - Reorganise

import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)
print()

b = a.reshape((8,1))
print(b)
print()
b = a.reshape((4,2))
print(b)
print()
b = a.reshape((2,2,2))
# b = a.reshape((2,3))  --- ERROR
print(b)
print()

# Vertically Stacking Vectors
v1 = np.array([1,2,3,4,])
v2 = np.array([5,6,7,8])

v3 = np.vstack([v1,v2])
print("v3 -\n",v3)

v3 = np.vstack([v1,v2,v1,v2])
print("\nv3 -\n",v3)

# Horizontal Stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

h = np.hstack((h1,h2)) # could also pass as a List
print("\nh -\n",h)
