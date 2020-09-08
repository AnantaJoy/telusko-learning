# recursion in function

def facto(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        return n*(facto(n-1))

n_facto = facto(5)
print(n_facto)

# find the recursion limit
import sys
print(sys.getrecursionlimit())
# sys.getrecursionlimit(2000)
# print(sys.getrecursionlimit())