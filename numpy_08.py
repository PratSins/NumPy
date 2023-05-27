# Load Data from file

import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32') # this line is needed as the default type is - float
print(filedata)