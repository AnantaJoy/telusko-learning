# check a number is wheather divisible by 5 or not

numbers = [12,13,43,14,15,23,53,55]
for num in numbers:
    if num%5 == 0:
        print(num)
        break
else:
    print("Not Found") 