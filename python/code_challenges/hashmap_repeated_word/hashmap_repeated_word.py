from code_challenges.hashmap_repeated_word.hash_table import Hashtable

def repeated_word(str):
    '''
    Finds the first word repeated in a string sentence.
    Input: str as a string
    Output: first repeated word
    '''
    #splits string sentence into individual words
    str_list = str.split(' ')
    #create an empty hash table
    ht = Hashtable()

    #iterate through the ist of words, sterilize them of puncuation, and store them in the hash table.
    for word in str_list:
        word = no_punc(word)
        #return the word if found in the hash table already
        if ht.contains(word) == True:
            return word
        else:
            ht.set(word,word)
    #raise an exception if no match found.
    raise Exception('No Match Found!')

def no_punc(word):
    '''
    Takes in a string and removes all puncuation from it and returns the stripped string.
    Input: word as a string
    Output: stripped string
    '''
    punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~+'''
    #iterate through the characters in the given string
    for ch in word:
        #if that character is found in the list of punctuation, remove it from the string.
        if ch in punc:
            word = word.replace(ch, "")

    word = word.lower()
    return word

print(repeated_word('Land a big one, jerk one.'))
