my_list = [1, 3, 5, 7, 9]
target = 5
def binary_search(arr, target):
    start = 0
    end = len(arr) -1
    mid = (start + end) // 2
    while start < end:
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            mid = (start + end) // 2
    return -1

print(binary_search(my_list, target))