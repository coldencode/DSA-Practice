def selection_sort(list):
    n = len(list)
    
    for i in range(n):
        current_min = float('inf')
        idx = i
        # Get current min
        for j in range(i, n):
            if current_min > list[j]:
                current_min = list[j]
                idx = j
        # Swap min elem with the front
        list[i], list[idx] = list[idx], list[i]
    
    return list

print(selection_sort([1,2,3,2,2,1]))
print(selection_sort([5,4,3,2,1]))
