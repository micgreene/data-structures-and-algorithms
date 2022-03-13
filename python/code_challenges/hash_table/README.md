# Hash Map Class

## Implement a Hash Map

### Challenge

+ **Implement a Hashtable Class with the following methods:**
  + **set**
    + Arguments: key, value
    + Returns: nothing
    + This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    + Should a given key already exist, replace its value from the value argument given to this method.
  + **get**
    + Arguments: key
    + Returns: Value associated with that key in the table
  + **contains**
    + Arguments: key
    + Returns: Boolean, indicating if the key exists in the table already.
  + **keys**
    + Returns: Collection of keys
  + **hash**
    + Arguments: key
    + Returns: Index in the collection for that key

### Approach & Efficiency

+ I started by creating the set function and ensuring it could create the expected data structure and store data properly.
+ I did some initial testing with hard coded values to first make sure that set() was working correctly, then I did some more as I added the hash function to set(). Once all tests were passing I continued.
+ I then created the contains function to be able to iterate through the hash table and find data.
+ contains() made the get function very simple since the logic is nearly the same, just with a different return value.
+ I was unsure as to how to tackle keys at first, but I did some research on how to unpack dictionaries into lists and this made it very simple.
