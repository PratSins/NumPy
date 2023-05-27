import numpy as np


f = np.linspace(1,5,12)
print("f - \n",f)
f = np.linspace(1,4,4)
print("f - ",f)
print()

emp = np.empty(2)
print("emp - ",emp)
print()

emp = np.empty((2,3))
print("emp - ",emp)
print()

eml = np.empty_like(f)
print("eml - ",eml)
print()

a = np.arange(18)
print("a - ",a)

b = a.reshape(2,9)
print("b = a.reshape(2,9) - \n",b)
# b = a.reshape(23,9) --- error
b = b.ravel()
print("b = b.ravel()   <-- Now its the same as np array a -->  --- ",b)
print()

x = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(x)
print("arr - \n",arr)
a_bool = arr > 5
print("a_bool - \n",a_bool)
print("arr[ a_bool ] - ",arr[a_bool])
print()

a2 = arr.sum(axis=0)
print("a2 = arr.sum(axis=0) - ",a2)
a2 = arr.sum(axis=1)
print("a2 = arr.sum(axis=1) - ",a2)
print()

# the following can't be done with lists
a3 = arr + arr
print("arr + arr - \n",a3)
a3 = arr * arr
print("arr * arr - \n",a3)