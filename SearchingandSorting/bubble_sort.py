def bubble_sort(lst):
    # Your code goes here
    for i in range(len(lst)-1, 0, -1):
        for j in range (i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

lst = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lst)
print(lst)