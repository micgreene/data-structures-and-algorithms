def quick_sort(lst, left, right):
    if len(lst) == 0:
        raise Exception('Empty List!')
    '''
    This function sorts a list through the quick method.
    Input: lst as a list of integers,
    left as an integer of the first index of list,
    right as an integer of the last index of list
    Output: a sorted list
    [8,4,23,42,16,15]
    '''
    if left < right:
        #Partition the array by setting the position of the pivot value
        position = partition(lst, left, right)
        #Sort the left
        quick_sort(lst, left, position - 1)
        #Sort the right
        quick_sort(lst, position + 1, right)
    else:
        print('cant')
    return lst

def partition(lst, left, right):
    #set a pivot value as a point of reference
    pivot = lst[right]
    #create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    for i in range(left, right):
        if isinstance(lst[i], int) != True:
            raise Exception('Current index not an integer! Exiting sort.')

        if lst[i] <= pivot:

            low = low + 1
            swap(lst, i, low)
    #place the value of the pivot location in the middle.
    #all numbers smaller than the pivot are on the left, larger on the right.
    swap(lst, right, low + 1)

    #return the pivot index point
    return low + 1

def swap(lst, i, low):
    temp = lst[i]
    lst[i] = lst[low]
    lst[low] = temp
