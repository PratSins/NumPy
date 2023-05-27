import numpy as np

b = np.array([ [ [1,2], [3,4] ],  [ [5,6], [7,8] ] ])
print("b -\n",b)
print()

print(b[0,1,1])
print(b[:,1,:])
print()


b[:,1,:] = [[9,9],[8,8]]
# b[:,1,:] = [[9,9,9],[8,8]]  --- GIVES ERROR
print("b -\n",b)
print()


c = np.zeros(5)
print("c - ", c)
c = np.zeros((2,3))
print("c -\n", c)
c = np.zeros((2,3,3)) # U can have as many dimensions as possible
print("c -\n", c)
print()

d = np.full((2,2),99,dtype='float64') # np.pi can also be used instead of 99
print("d -\n", d)
print()

a = np.array( [ [1,2,3,4,5,6,7], [8,9,10,11,12,13,14] ] )
d = np.full_like(a,4)
print("d -\n",d)
d = np.full_like(a.shape,4)
print("d - ",d)
d = np.full(a.shape,4)
print("d -\n",d)
print("\n\n")


e = np.arange(15)
print("e - ",e)
e = np.arange(2,8)
print("e - ",e)
e = np.arange(2.0,8.0)
print("e - ",e)
e = np.arange(2,8,0.5)
print("e - ",e)
print()

f = np.linspace(1,5,12)
print("f - ",f)
f = np.linspace(1,4,4)
print("f - ",f)
print()