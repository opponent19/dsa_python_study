def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    
    return -1


my_list = [10, 20, 33, 43, 50, 64, 70, 88]
target = 70
result = linear_search(my_list, target)
print(result)