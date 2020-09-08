
# check a number is odd or even by passing a list

def  checkNum(number):
    even = 0
    odd = 0

    for i in number:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


numbers = [1,3,8,6,83,72,17,77,37,36,5,3,72] 
odd, even = checkNum(numbers)
print("Even:{} and Odd:{}".format(even,odd))