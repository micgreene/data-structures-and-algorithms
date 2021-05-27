# Hashtables

Hash Tables utilize linked lists stored in array indexes to group items automatically within a certain range of indexes. The main feature of a Hash Map is the ability to hash the key portion of your key:value pair and use the hashed number to give it a predictable array index which can be used to locate the value.

## Challenge

**Implement a Hashtable with the following methods:**

- **add:** takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- **get:** takes in the key and returns the value from the table.

- **contains:**  takes in the key and returns a boolean, indicating if the key exists in the table already.

- **hash:** takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency

For this assignment I used TDD to approach this. I created a test case for each of the assigned unit tests then solved for the problem as I went. This allowed me to finish all the methods except for the 'contains()' method simply with TDD, and it being so similar to the 'get()' made it a simple matter to finish it afterwards.

## API

N/A