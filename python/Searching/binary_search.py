pos = 0
def search(list,target):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u)//2

        if list[mid] == target:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < target:
                l = mid + 1
            else:
                u = mid - 1


new_list = [13,36,35,57,64,78,82,93]

if search(new_list, target=84):
    print("Found")
else:
    print("Not Found")