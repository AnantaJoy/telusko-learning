# square using '#'
i = 1
j = 1
while i<=4:
    while j<=4:
        print("# ", end="")
        j+=1  
    print()
    i+=1
    j=1
    

# u can print using for loop also 
# for i in range(4):
#     for j in range(4):
#         print("# ",end="")
#     print()

# draw a triangle
for i in range(4):
     for j in range(i+1):
         print("# ",end="")
     print()

# reverse triangle
for i in range(4):
     for j in range(4-i):
         print(j,"",end="")
     print()