from code_challenges.hashmap_left_join.hash_table import Hashtable

def left_join(ht1, ht2):
    '''
    Takes in two hashtables and perform a simplified left join on them. THis means the first table (the left table) will store all of its key value pairs in a list of lists. For each matching key in the second table, append the value of that key to the corresponding list. Returns the list of lists.
    Input: ht1, ht2 as Hashtables
    Output: 2d list
    '''
    ret_list = []

    for pair in ht1.bucket:
        #most of the hashmap is None, make sure we are not dealing with a None value
        if pair is not None:
            #doublecheck value is a string and nothing else
            if isinstance([ *pair.items()][0][0], str) == False or isinstance([ *pair.items()][0][1], str) == False:
                raise Exception('Must be a string value.')

            #create a list with a length of 3, all indexes assigned as None
            lst = 3 * [None]

            #assign the first 2 indexes of the list as the key value pair from the dictionary
            lst[0] = [ *pair.items()][0][0]
            lst[1] = [ *pair.items()][0][1]

            #append this new list to the return list
            ret_list.append(lst)

    for pair in ht2.bucket:
        #most of the hashmap is None, make sure we are not dealing with a None value
        if pair is not None:
            #doublecheck value is a string and nothing else
            if isinstance([ *pair.items()][0][0], str) == False or isinstance([ *pair.items()][0][1], str) == False:
                raise Exception('Must be a string value.')

            #create a temp value and counter
            temp = ret_list[0]
            count = 0

            #iterate through list until we find all matches
            while count < len(ret_list):
                #if we find a match, append the value of that key to its matching list
                if temp[0] == [ *pair.items()][0][0]:
                    temp[2] = [ *pair.items()][0][1]

                #increment the count and assign temp as the next index in the list
                count = count + 1
                if count < len(ret_list):
                    temp = ret_list[count]

    return ret_list
