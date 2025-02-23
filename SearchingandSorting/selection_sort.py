def selection_sort(lst):
    # Your code goes here
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst
lst = [64, 34, 25, 12, 22, 11, 90]
selection_sort(lst)
print(lst)