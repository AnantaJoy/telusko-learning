fileA = open('readme.txt','r')

print(fileA.read())

# write a file
fileB = open('sample','w')
# fileB.write('sample text')

# file = fileB.write("Write something on fileB")

# for txt in fileB:
#     print(txt)

#  read write and append in python

# print a image value

f = open('sumaiya.jpg','rb')

# for i in f:
#     print(i)

f1 = open('sumu.jpg','wb')

for i in f:
    f1.write(i)