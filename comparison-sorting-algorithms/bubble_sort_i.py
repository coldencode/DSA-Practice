def bubble_sort(list):
    end_boundary = len(list)
    for i in range(len(list)):
        for j in range(0, end_boundary-i-1):
            if list[j] > list[j+1]:
                swap(list, j, j+1)
            else:
                continue
    
    return list

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

print(bubble_sort([1,2,3,2,2,1]))
print(bubble_sort([5,4,3,2,1]))