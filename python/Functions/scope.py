## Global Vs Local

msg = 'Global' 

def scope():
    global msg2
    msg = 'Local'
    msg2 = 'Local 2'
    print(msg)
    print(msg2)

print(msg)
scope()
print(msg2)