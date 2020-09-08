# import an array
from array import *

# areate an empty array
arr = array('i',[])

# ask user to input the size of an array
n = int(input("Enter the length of an array:"))

# ask user to input array values
for i in range(n):
    x = int(input("Enter array  values:"))
    arr.append(x)
print(arr)

src_value = int(input("Enter a value to search:"))

for e in arr:
    if e==src_value:
        print("Found the value")
        break
else:
    print("No value found")