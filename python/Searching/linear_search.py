# linear search
pos = -1
def search(lst,target):
    for i in lst:
        if i == target:
            # globals() ['pos'] = i
            return True
            break

    return False
    

list_A = [1,3,5,7,9]

if search(list_A, target=9):
    print('Found in posion',pos)
else:
    print("Not Found")