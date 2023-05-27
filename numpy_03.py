import numpy as np

a = np.random.rand(4)
print("\na = ",a)
a = np.random.rand(4,2)
print("\na = ",a)
a = np.random.rand(4,2,3)
print("\na = ",a)
print("\n\n")

k = np.random.randint(0,9,size=(5,10))
print("k -\n",k)
print("\n\n")

a = np.array( [ [1,2,3,4,5,6,7], [8,9,10,11,12,13,14] ] )
print("a = ",a)
b = np.random.random_sample(a.shape)
print("\nb = ",b) 
print("\n\n")


c = np.random.randint(7, size=(3,3))
print("c = \n",c)
c = np.random.randint(4,7, size=(3,3))
print("c = \n",c)
c = np.random.randint(-4,7, size=(3,3))
print("c = \n",c)
# the argument before size=() is the rage within which the elements are generated
print("\n\n")

d = np.identity(3)
print("d - \n",d)
print("d.shape - ",d.shape)
print("\n\n")

r1 = np.array([1,2,3,4,])
e = np.repeat(r1, 3)
print("e - ",e)

r2 = np.array([[1,2,3,4,]])
f = np.repeat(r2, 3, axis=0)
print("f - \n",f)
f = np.repeat(r2, 3, axis=1)
print("f - ",f)
# f = np.repeat(r2, 3, axis=2)  ----> Error
print("\n\n")

lst = [[1,1,1,1,1], 
       [1,0,0,0,1], 
       [1,0,9,0,1],
       [1,0,0,0,1],
       [1,1,1,1,1]]
g = np.array(lst)
print("g -\n",g)
print("\n\n")

h = np.ones((5,5))
print("h -\n",h)
i = np.zeros((3,3))
i[1,1] = 9
print("i -\n",i)
print("\n Editting NP-arr h - ")
h[1:4,1:4] = i
print("h -\n",h)

print("\nNP-arr h is the same ad g")