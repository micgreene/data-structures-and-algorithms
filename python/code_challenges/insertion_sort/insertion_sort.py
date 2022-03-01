def insertion_srt(lst):
    '''
    This function sorts a list through the insertion method.
    Input: lst as a list of integers
    Output: a sorted list
    '''
    if len(lst) == 0:
        raise Exception('Empty List!')

    for i in range(1,len(lst)):
        if isinstance(lst[i], int) != True:
            raise Exception('Current index not an integer! Exiting sort.')

        j = i - 1
        temp = lst[i]

        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = temp

    return lst
