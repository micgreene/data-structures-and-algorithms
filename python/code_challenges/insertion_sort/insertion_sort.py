def insertion_srt(lst):
    '''
    This function sorts a list through the insertion method.
    Input: lst as a list of integers
    Output: a sorted list
    '''
    for i in range(1,len(lst)):
        j = i - 1
        temp = lst[i]

        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = temp

    return lst
