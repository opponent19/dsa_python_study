def selection_sort(lst):
    
    n = len(lst)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst
                
lst = [64, 25, 12, 22, 11]
result = selection_sort(lst)
print(result)