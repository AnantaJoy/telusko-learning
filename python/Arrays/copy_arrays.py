from numpy import *

arr1 = array([1,2,3,4,5,6])
arr2 = array([7,8,9,10,11,12])
# add five to every element
# arr1 += 5
# print(arr1)
# copy of an array

# shallow copy
arr = arr1.view()
print(arr)
print(id(arr1))
print(id(arr))
# deep copy
arr = arr1.copy()
print(arr)
print(id(arr))
print(id(arr1))

# add two array
arr3 = arr1 + arr2
print(arr3)
# sqrt of an array
print(sqrt(arr1))
# min and max
print(min(arr3))
print(max(arr2))