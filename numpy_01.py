import numpy as np
import warnings
warnings.simplefilter('ignore')


myarr = np.array([3,6,32,7])
print("myarr - ",myarr)
print("myarr.ndim - ",myarr.ndim)
print("myarr[0] - ",myarr[0])
print("myarr.shape - ",myarr.shape)
print("myarr.dtype - ",myarr.dtype)
print()

print("\n numpy can also accept dicionary as input -- NOT RECOMMENDED\n")
k = np.array({1,2,3,2})
print("k <created using dict> - ",k)
print("k.dtype  -- ",k.dtype)
print()

myarr2 = np.array([3,6,377772,7], np.int8)  # ---- gives warning
print("myarr2(int8) - ",myarr2)
myarr2 = np.array([3,6,377772,7], np.int64)
print("myarr2(int64) - ",myarr2)
print()

myarr1 = np.array([[3,6,32,7]])
print("myarr1 - ",myarr1)
print("myarr1.shape - ",myarr1.shape)
print("myarr1[0,2] - ",myarr1[0,2])
print("myarr1.dtype - ",myarr1.dtype) # google Search --> NumPy types Reference
print()

myarr1[0,2] = 233
print("myarr1 (after change) - ",myarr1)
print()

a = np.array( [1,2,3], dtype='int16')
print("a - ", a)
print("a.dtype - ",a.dtype)
print("a.itemsize - ",a.itemsize)
print("a.size <-total no. elements-> - ",a.size)
print("a.nbytes <-total size in bytes of NP array-> - ",a.nbytes)
print()

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print("b -\n",b)
print("b.ndim - ",b.ndim)
print("b.shape - ",b.shape)
print("b.dtype - ",b.dtype)
print("b.itemsize - ",b.itemsize)  # returns the size in bytes of each element
print("b.size <-total no. elements-> - ",b.size)
print("b.nbytes <-total size in bytes of NP array-> - ",b.nbytes)
print()

c = np.array( [ [1,2,3,4,5,6,7], [8,9,10,11,12,13,14] ] )
print("c -\n",c)
print("\nc[1,5] - ",c[1,5])
print("c[1,-2] - ",c[1,-2])
print("c[0,:] - ",c[0,:])
print("c[0,1:6:2] - ",c[0,1:6:2])
print("c[0,1:6:-2] - ",c[0,1:6:-2])
print("c[0,1:-2:2] - ",c[0,1:-2:2])
print("c[0,1:-1:2] - ",c[0,1:-1:2])
print()

c[1,5] = 20
print(c,"\n")
c[:,2] = 5
print(c,"\n")
c[:,2] = [1,2]
print(c,"\n")


a = np.array([1,2,3])
b = a
print("a - ",a)
print("b - ",b)
b[0] = 100
print("a - ",a)