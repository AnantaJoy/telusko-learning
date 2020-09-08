# fibonacci series

def fibo(n):
    n1=0
    n2=1
    for i in range(2,n):
        nexnum = n1+n2
        n1 = n2
        n2 = nexnum
        # print(nexnum)
    print(nexnum)


nth = int(input("Enter the len of the series: "))
fibo(nth)