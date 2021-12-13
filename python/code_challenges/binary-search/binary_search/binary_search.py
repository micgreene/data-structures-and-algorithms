test_list1 = [4, 8, 15, 16, 23, 42]
test_list2 = [-131, -82, 0, 27, 42, 68, 179]
test_list3 = [11, 22, 33, 44, 55, 66, 77]
test_list4 = [1, 2, 3, 5, 6, 7]

def binary_search(list, key):
    '''
    Given a sorted list and a key value(int), performs a binary search on the list and returns the index of the key value in the list. If the key value does not appear in the list or the list is empty, return -1 instead.

    Input: list, int
    Output: int
    '''
    #if the list is empty, return -1
    if len(list) == 0:
        return -1

    start_index = 0
    end_index = (len(list) - 1)

    #base case checks to see where the first index and last index being checked are, once they are both assigned to the same index or begin to 'pass' eachother, the loop ends
    while start_index <= end_index:
        #find the middle index of the list
        mid = (start_index + end_index)//2

        #if the key value matches the middle index then just return the middle index
        if key == list[mid]:
            return mid

        #if not:
            #if the key value is less than the middle point move the last point to be checked the index prior to the middle index (the numbers past this index are larger and thus not correct)
            #if the key value is greater than the middle point move the first point to be checked the index immediately after the middle index (the numbers prior to this index are smaller and thus not correct)
        elif key < list[mid]:
            end_index = mid - 1
        elif key > list[mid]:
            start_index = mid + 1

    #if no index can be found return -1
    return -1

print(f'Test 1 - list: {test_list1}, key: {15} ---> {binary_search(test_list1, 15)}\n')
print(f'Test 2 - list: {test_list2}, key: {42} ---> {binary_search(test_list2, 42)}\n')
print(f'Test 3 - list: {test_list3}, key: {90} ---> {binary_search(test_list3, 90)}\n')
print(f'Test 4 - list: {test_list4}, key: {4} ---> {binary_search(test_list4, 4)}\n')
