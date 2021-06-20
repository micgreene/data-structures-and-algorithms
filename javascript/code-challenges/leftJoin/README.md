# Code Challenge: Class 33 - LEFT JOIN

Hash Tables utilize linked lists stored in array indexes to group items automatically within a certain range of indexes. The main feature of a Hash Map is the ability to hash the key portion of your key:value pair and use the hashed number to give it a predictable array index which can be used to locate the value.

## Challenge

**Implement a simplified LEFT JOIN for 2 Hashmaps.**

- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.

- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.

- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.

  - If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Approach & Efficiency

For this assignment I used the console to test.

- First I created a hashmap and then a simple function that printed out its values.

- I then created logic that printed out just the keys of all map values, even in cases of collisions.

- After this, I used a .map() function to compare each key in the left hashmap to each key in the right hashmap.

- In cases where they matched, I had to figure out to reassign the value using string concatenation.

## API

N/A