# Code Challenge 13 - Multi-bracket Validation.

## Challenge

### Write a function called validate brackets

+ Arguments: string
+ Return: boolean representing whether or not the brackets in the string are balanced
+ There are 3 types of brackets:
  + Round Brackets : ()
  + Square Brackets : []
  + Curly Brackets : {}

### Whiteboard

![Whiteboard](stack_queue_animal_shelter.jpg)

### Approach & Efficiency

+ I started by copying over Node and Stack scripts to help with importing errors.
+ With this, I could test each data structure.
+ I then started with the bracket_validation function
  + I used a whiteboard to lay out the string as a list. This allowed me to see the problem better.
  + I then determined a loop would be good to process each item in the list.
  + I determined that the only thing that needs to be checked really is that if a closed bracket is found, it should match a open bracket immediatly from the stack or something went wrong. This informed me as to what my algorithm should look like.
  + I then did one last pass of the function, using the unit test conditions to determine edge cases.
