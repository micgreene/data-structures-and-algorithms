import sys

sys.path.append('/home/micgreene/codefellows/301/data-structures-and-algorithms/python/code_challenges/linked-list/linked_list')

from linked_list import Node, Linked_List

def zip_lists(list1, list2):
    '''
    Zip two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
    Input: ll1, ll2 as Linked Lists
    Output: ret_list as a Linked List
    '''
    if list1.head is None and list2.head is None:
        return None

    ret_list = Linked_List()
    ll1, ll2 = list1.head, list2.head

    while ll1 or ll2:
        if ll1:
            ret_list.append(ll1.value)
            ll1 = ll1.next
        if ll2:
            ret_list.append(ll2.value)
            ll2 = ll2.next

    return ret_list
