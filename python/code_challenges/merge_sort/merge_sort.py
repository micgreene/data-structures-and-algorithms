import math

def merge_sort(lst):
    '''
    This function sorts a list through the merge method.
    Input: lst as a list of integers
    Output: a sorted list
    '''
    n = len(lst)
    if n > 1:
        mid = math.floor(n/2)
        left = lst[0:mid]
        right = lst[mid:n]
        #sort the left side
        merge_sort(left)
        #sort the right side
        merge_sort(right)
        #merge the sorted left and right sides together
        merge(left, right, lst)

    return lst

def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1
    if i == len(left):
        for num in range(j,len(right)):
            lst[k] = right[j]
            j = j + 1
            k = k + 1
    else:
        for num in range(i,len(left)):
            lst[k] = left[i]
            i = i + 1
            k = k + 1

print(merge_sort([8,4,23,42,16,15]))
print(merge_sort([20,18,12,8,5,-2]))
print(merge_sort([5,12,7,5,5,7]))
print(merge_sort([2,3,5,7,13,11]))

