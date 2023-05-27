import numpy as np
import warnings
warnings.simplefilter('ignore')

x = [0,1,2,3,4,5,6,7,8,9,10]
arr = np.array(x)
print("arr - ",arr)
print()

d = arr-100
print("arr-100 - ",d)
print()

d = arr/arr
print("---warnings---")
print("arr/arr - ",d)
d = 1/arr
print("1/arr - ",d)
print()

d = arr ** 2
print("d - ",d)
print()

e = np.sqrt(2)
print("e - ",e)
e = np.sqrt(d)
print("e - ",e)
print("e.max() - ",e.max())
print()

e = np.exp(d)
print("e - ",e)
e = np.sin(d)
print("e - ",e)
e = np.log(d) # warnings
print("e - ",e)
print()

x = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(x)
print("arr - \n",arr)
b = arr.T
print("arr.T - \n",b)
print("arr.ndim - ",arr.ndim)
print()

# arr.flat is an iterator
for i in arr.flat:
    print(i,end=" ")
print()
print()

