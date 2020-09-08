# import array as arr
from array import *

# arrays only holds same types data
values = array('i',[22,32,51,-54,35,15,94])
print(values)

# reverse an array 
values.reverse()
print(values)

# indexing array
print(values[2:4])

# size of an array
print(values.buffer_info())

# loops
for i in values:
    print(i)

# loops using range
for i in range(4):
    print(values[i])

# create a new array
newValues = array(values.typecode,(a for a in values))
print("Copy an array to a new array:")
for i in newValues:
    print(i)

# while loop
print("Using while loops:")
i = 0
while i<len(newValues):
    print(newValues)
    i+=1
