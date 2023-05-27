# NumPy - Statistics

import numpy as np

stats = np.array([[1,2,3], [4,5,6]])
print("stats -\n",stats)
print()

k = np.min(stats)
print("Min in stats array - ", k)
k = np.max(stats)
print("Max in stats array - ", k)
print()

k = np.min(stats, axis=0)
print("axis=0 - Min in stats array - ", k)
k = np.min(stats, axis=1)
print("axis=1 - Min in stats array - ", k)
k = np.max(stats, axis=0)
print("axis=0 - Max in stats array - ", k)
k = np.max(stats, axis=1)
print("axis=1 - Max in stats array - ", k)
print()

k = np.sum(stats)
print("Sum of all the elements of stats = ",k)
k = np.sum(stats, axis=0)
print("axis=0 - Sum of all the elements of stats = ",k)
k = np.sum(stats, axis=1)
print("axis=1 - Sum of all the elements of stats = ",k)
print()

print("stats.mean - ",stats.mean())