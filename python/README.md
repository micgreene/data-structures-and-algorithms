# Data Structures and Algorithms

## Language: `Python`

## Code Challenges

+ Code Challenge 01: [Array Reverse](code_challenges/array_reverse/README.md)
+ Code Challenge 02: [Insert Shift Array](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/array_insert_shift/README.md)
+ Code Challenge 03: [Binary Search](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/binary-search/README.md)
+ Code Challenge 04: [Interview 01](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/fib-seq/README.md)
+ Code Challenges 05 - 07: [Linked List](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/linked-list/README.md)
+ Code Challenge 08: [Zip Two Linked Lists](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/linked-list-zip/README.md)
+ Code Challenges 10: [Stack and Queue](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/stack_and_queue/README.md)
+ Code Challenges 11: [Implement a Queue using two Stacks](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/stack_queue_pseudo/README.md)
+ Code Challenges 12: [First-in, First out Animal Shelter](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/stack_queue_animal_shelter/README.md)
+ Code Challenges 13: [Multi-bracket Validation](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/stack_queue_bracket/README.md)
+ Code Challenges 15: [Binary Tree and BST Implementation](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/trees/README.md)
+ Code Challenges 16: [Maximum Value in a Binary Tree](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/trees/README.md)
+ Code Challenges 17: [Traverse Breadth-First Through a Binary Tree](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/tree_breadth_first/README.md)
+ Code Challenges 26: [Insertion Sort](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/insertion_sort/README.md)
+ Code Challenges 27: [Merge Sort](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/merge_sort/README.md)
+ Code Challenges 28: [Quick Sort](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/quick_sort/README.md)
+ Code Challenges 30: [Hash Tables](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/hash_table/README.md)
+ Code Challenges 31: [First Repeated Word](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/hashmap-repeated-word/README.md)
+ Code Challenges 32: [Common Values in 2 Binary Trees](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/tree-intersection/README.md)
+ Code Challenges 33: [Simplified LEFT JOIN for 2 Hashmaps](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/hashmap-left-join/README.md)
+ Code Challenges 35: [Implementation: Graphs](https://github.com/micgreene/data-structures-and-algorithms/blob/master/python/code_challenges/cc35-graph/README.md)

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
