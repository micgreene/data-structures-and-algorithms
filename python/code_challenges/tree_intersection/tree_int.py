from code_challenges.tree_intersection.binary_search_tree import BinarySearch
from code_challenges.tree_intersection.hash_table import Hashtable

def tree_intersection(tree1, tree2):
    '''
    Takes in two binary search trees and returns a set of values common to both.
    Input: tree1/tree2 as a BST
    Output: list of common values
    '''
    ht = Hashtable()
    ret_list = []

    #creates two lists containing the values of the trees
    values_list1 = tree1.in_order()
    values_list2 = tree2.in_order()

    #iterate through the first list, store all values in a hash tables
    for value in values_list1:
        if isinstance(value,int) == False:
            raise Exception('Not an Integer value!')

        ht.set(str(value), value)

    #iterate through the second list, all values found in hash table are appended to ret_list
    for value in values_list2:
        if isinstance(value,int) == False:
            raise Exception('Not an Integer value!')

        if ht.contains(str(value)) == True:
            ret_list.append(value)

    return ret_list
