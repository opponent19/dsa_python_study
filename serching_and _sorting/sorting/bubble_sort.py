
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr 

lst = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(lst)
print(result)