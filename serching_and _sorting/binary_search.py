
def binary_search(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2 
        if target == arr[mid]:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid + 1

my_list = [10, 25, 30, 45, 50, 70, 80]
target = 70

result = binary_search(my_list, target)
print(result)