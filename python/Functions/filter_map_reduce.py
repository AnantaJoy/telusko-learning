# list of numbers
numbers = [1,2,4,3,9,4,83,4]

# filer
even = list(filter(lambda n: n%2==0,numbers))
print(even)

# map
# double the even values
doubles = list(map(lambda n: n*2,even))
print(doubles)

# reduce
from functools import reduce
sums = reduce(lambda a,b: a+b,doubles)
print(sums)