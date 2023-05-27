# NumPy - Linear Algebra

import numpy as np

a = np.ones((2,3))
print("a -\n",a)
b = np.full((3,2), 2)
print("b -\n",b)
print("\n")

c = np.matmul(a,b)
print("Matrix Multiplication of NP-arr a and b")
print("c -\n",c)
print("\n")

d = np.identity(3)
print("d -\n",d)
print("\nDeterminant of NP-arr/Matrix d ---> ", end="")
k = np.linalg.det(d)
print(k)