def insertion_sort(list):
    pointer = 1
    n = len(list)
    while pointer != n:
        pos = pointer
        for i in range(pointer):
            if list[i] > list[pointer]:
                pos = i
                break
        # Shift
        shift(list, pos,pointer)
        pointer += 1
    
    return list
        

def shift(list, i, j):
    temp = list[j]
    for k in range(j, i, -1):
        list[k] = list[k-1]
    
    list[i] = temp

print(insertion_sort([1,2,3,2,2,1]))
print(insertion_sort([5,4,3,2,1]))
