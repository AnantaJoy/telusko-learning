# check a number is prime or not

num = int(input("Input a number to check Prime:"))

for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")