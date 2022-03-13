class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.bucket = size *[None]

    def set(self, key, value):
        '''
        Takes a key:value pair, hashes the key to find a (probably) empty index in our hash table and appends it there to the bucket. If the index is already assigned a value, create a dictionary in that bucket and continue storing pairs in new dictionary indexes.
        Input: key as a string,
               value as any value
        Output: None
        '''
        hash =  self.hash(key)

        #If the bucket is empty, create a new dictionary there. This will handle any collisions made in the future.
        if self.bucket[hash] == None:
            self.bucket[hash] = {}

        self.bucket[hash][key] = value

    def get(self, key):
        '''
        Takes a key and attempts to retrieve its value from the Hash Map if it exists. If not, throws an exception.
        Input: key as a string
        Output: value of key
        '''
        #1-hash the key
        hash = self.hash(key)

        #2-if dictionary is empty then raise exception
        if self.bucket[hash] == None:
            raise Exception('Value not found')

        #3-traverse through dictionary until matching key is found and return value
        for idx in self.bucket[hash]:
            if idx == key:
                return self.bucket[hash][key]

        #4 - if no key is present in the hash map raise an exception
        raise Exception('Value not found')

    def contains(self, key):
        '''
        Takes a key and returns true if that key can be found in the hash map.
        Input: key as a string
        Output: Boolean
        '''
        #1-hash the key
        hash = self.hash(key)

        #2-if dictionary is empty then return false
        if self.bucket[hash] == None:
            return False

        #3-traverse through dictionary until matching key is found and return true
        for idx in self.bucket[hash]:
            if idx == key:
                return True

        #4-if no matching key is found, return false
        return False

    def hash(self, key):
        '''
        Takes a key and returns a hashed value to be used as the index to store a value in the hash map.
        Input: key as a string
        Output: hashed string value
        '''
        #sum acts as an accumulator to track sum of all ascii values
        sum = 0

        #checks to see if key is an integer instead of a string
        if isinstance(key, int):
            raise Exception('Key cannot be integer')

        #iterates through string and converts each character into its ascii value
        for ch in key:
            if isinstance(ch, int):
                #if there was an int as part of the string use its value
                sum += ch
            else:
                # convert to ascii
                sum += ord(ch)

        primed = sum * 97
        index = primed % self.size

        return index

    def keys(self):
        '''
        Returns a collection of all keys in the dictionary.
        Input: None
        Output: List of keys
        '''
        ret_list = []

        for idx in self.bucket:
            if idx != None:
                #unpacks all key values in the dictionary as a temp list
                temp = [*idx]
                #appends the temp list to the total list of keys
                ret_list += temp

        return ret_list

has = Hashtable()

has.set('apple1',7)
has.set('apple',9)
has.set('pear',5)
has.set('grape',3)
has.set('orange',4)
print(has.get('apple2'))

print(has.keys())
