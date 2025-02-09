my_list = [10, 23, 45, 70, 11]
target = 70

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1
        
print(linear_search(my_list, target))