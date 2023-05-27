import numpy as np
import sys

one = np.array([1,3,4,634,2])
print("one - ",one)

k = one.argmax() # -- position of maximum element
print("k - ",k)
k = one.argmin() # -- position of minimum element
print("k - ",k)
print()

two = one.argsort()  # -- returns the an array with the positions of the elements sorted for the their respective values
print("two - ",two)
print()

y = [[1,2,3], [4,5,6], [77,8,0]]
x = np.array(y)
print("x - \n",x)
k = x.argmax()
print("k - ",k)
k = x.argmin()
print("k - ",k)
k = x.argmax(axis=0)
print("k - ",k)
k = x.argmax(axis=1)
print("k - ",k)
print()

z = x.argsort()
print("z - \n",z)
z = x.argsort(axis=0)
print("z - \n",z)
z = x.argsort(axis=1)
print("z - \n",z)
print()

w = np.where(x>5)
print("w - ",w,end="\n\n")
print("type(w) - ",type(w))
print("np.count_nonzero(x) - ",np.count_nonzero(x))
print()

w = np.nonzero(x)
print("w - ",w,end="\n\n")

py_ar = [0,4,55,2]
np_ar = np.array(py_ar)
k = sys.getsizeof(1) * len(py_ar)
print("k - ",k)
k = np_ar.itemsize * np_ar.size
print("k - ",k)

