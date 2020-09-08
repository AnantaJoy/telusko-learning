from numpy import *

arr1 = array([
                [1,2,3,2,3,4],
                [3,4,5,3,4,2],
            ])
print(arr1)
# dimension of an array
print(arr1.ndim)
# shape of an array
print(arr1.shape)
# size of an array
print(arr1.size)
# multi dimension to single dimension
print(arr1.flatten())
# single to multi dimension
print(arr1.reshape(3,2,2))

# matrices
m = matrix("1 2 3; 2 3 4; 3 2 4")
print(m)