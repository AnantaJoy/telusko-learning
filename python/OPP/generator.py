def topten():
    
    n = 1

    while n<=10:
        sqr = n*n
        yield sqr
        n += 1


values = topten()

print(values.__next__())

for i in values:
    print(i)