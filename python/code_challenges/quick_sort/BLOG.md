# Quick Sort

## Author: Michael Greene

### Introduction

**In this article we will review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample list.**

**I will then show the step-by-step output after each iteration.**

## Pseudocode

**Line #**
1- `ALGORITHM QuickSort(arr, left, right)`
2-    `if left < right`
3-        `// Partition the array by setting the position of the pivot value`
4-        `DEFINE position <-- Partition(arr, left, right)`
5-        `// Sort the left`
6-        `QuickSort(arr, left, position - 1)`
7-        `// Sort the right`
8-        `QuickSort(arr, position + 1, right)`
9-`ALGORITHM Partition(arr, left, right)`
10-    `// set a pivot value as a point of reference`
11-    `DEFINE pivot <-- arr[right]`
12-    `// create a variable to track the largest index of numbers lower than the defined pivot`
13-    `DEFINE low <-- left - 1`
14-    `for i <- left to right do`
15-        `if arr[i] <= pivot`
16-            `low++`
17-            `Swap(arr, i, low)`
18-     `// place the value of the pivot location in the middle.`
19-     `// all numbers smaller than the pivot are on the left, larger on the right.`
20-     `Swap(arr, right, low + 1)`
21-    `// return the pivot index point`
22-     `return low + 1`
23-`ALGORITHM Swap(arr, i, low)`
24-    `DEFINE temp;`
25-    `temp <-- arr[i]`
26-    `arr[i] <-- arr[low]`
27-    `arr[low] <-- temp`

### Algorithm

*For this example, we will use a sample list:*
**[8,4,23,42,16,15]**

1. The first line of code, `ALGORITHM QuickSort(arr, left, right)`, tells us this is a function.

+ This function takes in 3 parameters:
  + arr: a list of integers
    + **arr = [8,4,23,42,16,15]**
  + left: the first index of the list (will start as 0)
    + **left = 0**
  + right: the last index of the list (will start as list length - 1)
    + **right = 5**

1. The second line, `if left < right`, checks if the left index we are checking is less than the right index. This will cause this process to stop once the lower index surpasses the greater.

+ **Note:** This keeps our function from going out of range of the given list.
  + **0 < 5:**

1. Line 4, `DEFINE position <-- Partition(arr, left, right)`, is calling an outside function, Partition(), to separate the list using a pivot point.

+ **Note:** This brings our logic into the Partition() function beginning on line 9.
  + **partition([8,4,23,42,16,15], 0, 5)**

1. On line 9, `ALGORITHM Partition(arr, left, right)`, tells us we have a new function that will take the same list and left/right parameters as quickSort().

+ Line 11, `DEFINE pivot <-- arr[right]`, creates a new variable 'pivot', which is assigned the value of the list index at right. (arr[right])
  + This index will act as our pivot point against which the rest of indexes wil be compared.
    + **pivot = 15**
+ Line 13, `DEFINE low <-- left - 1`, creates a variable to track the largest index of numbers lower than the defined pivot point.
  + **low = -1**
+ Line 14, `for i <- left to right do`, begins a for loop that ranges between the left index position and one index shy of the right index position. (i = 0 - 4)
  + i = 0:
    + Line 15, `if arr[i] <= pivot`, compares the current index with the pivot point.
      + **8 <= 15:**
    + Line 16, `low++`, increments the low index tracker.
      + **low = 0**
    + Line 17, `Swap(arr, i, low)`, calls the outside function swap() to change the positions of two indexes.
    + In this case, nothing happens since both i and low = 0.
      + list = [8,4,23,42,16,15]

  + i = 1:
    + 4 <= 15:
    + low = 1
    + [8,4,23,42,16,15]

  + i = 2:
    + Here, 23 is not less than or equal to 15, so nothing happens.

  + i = 3:
    + Here, 42 is not less than or equal to 15, so nothing happens.

  + i = 4:
    + Here, 16 is not less than or equal to 15, so nothing happens.

  + Line 20, `Swap(arr, right, low + 1)`, swaps our pivot point with the index that is one after the index that the low counter was incremented to.
    + **arr = [8,4,15,42,16,23]**
  + Line 22, `return low + 1` returns the index position that pivot index was swapped to.
    + **returns 2**
    + **Note:** This marks the index where the left and right sides of the list are separated. This ends the logic inside of Partition().

1. On line 6, quicksort() calls itself recursively now that the list has been partitioned.

+ **FIRST RECURSION**
+ quicksort([8,4,15,42,16,23], 0, 1):
  + **left = 0**
  + **right = 1**
  + 0 < 1:
    + partition([8,4,15,42,16,23], 0, 1):
      + pivot = 4
      + low = -1
      + `for i <- 0 to 1 do`
        + i = 0:
          + 8 !<= 4
      + `Swap(arr, right, low + 1)`
        + **list = [4,8,15,42,16,23]**
      + `return low + 1`
        + **returns 0**
      + **Note:** Anytime our Partition() returns 0 or 1, this will mean the end of that recursion since left < right is the base case to continue quickSort().

+ **SECOND RECURSION**
+ Since quicksort() is recursive, this is what happens the second time we try to call quicksort() on the left side of the list using our return index.
+ quicksort([4,8,15,42,16,23], 0, 0):
  + left = 0
  + right = 0
  + 0 can't be less than 0 so this function ends.

+ **FIRST RECURSION**
+ Since the second recursion could not continue, we now resolve the rest of our first recursion using line 8, `QuickSort(arr, position + 1, right)`.
  + quicksort([4,8,15,42,16,23], 3, 5):
    + **left = 3**
    + **right = 5**
    + 3 < 5:
      + partition([4,8,15,42,16,23], 3, 5):
        + pivot = 23
        + low = 2
        + `for i <- 3 to 5 do`
          + i = 3:
            + 42 !<= 23
          + i = 4:
            + 16 <= 23:
            + low = 3
            + `Swap(arr, i, low)`
              + **list = [4,8,15,16,42,23]**
        + `Swap(arr, right, low + 1)`
          + **list = [4,8,15,16,23,42]**
        + `return low + 1`
          + **returns 4**

+ *NEW* **SECOND RECURSION**
+ While the first quickSort() recurision could not continue, the recursion on Line 8 is able to continue its own recursion:
  + Line 6, `QuickSort(arr, left, position - 1)`: **quicksort([4,8,15,16,23,42], 0, 3)**:
    + **left = 0**
    + **right = 3**
    + 0 < 3:
      + partition([4,8,15,16,23,42], 0, 3):
      + pivot = 16
      + low = -1
      + `for i <- 0 to 3 do`
        + i = 0:
          + 4 <= 16:
            + low = 0
            + `Swap(arr, i, low)`
              + **[4,8,15,16,23,42]**
        + i = 1:
          + 8 <= 16:
            + low = 1
            + `Swap(arr, i, low)`
              + **[4,8,15,16,23,42]**
        + i = 2:
          + 15 <= 16:
            + low = 2
            + `Swap(arr, i, low)`
              + **[4,8,15,16,23,42]**
      + `Swap(arr, right, low + 1)`
        + **[4,8,15,16,23,42]**
      + `return low + 1`
        + **returns 2**

+ **THIRD RECURSION**
+ Line 6, `QuickSort(arr, left, position - 1)`: quicksort([4,8,15,16,23,42], 0, 1):
  + **left = 0**
  + **right = 1**
  + 0 < 1:
    + partition([4,8,15,42,16,23], 0, 1):
    + pivot = 8
    + low = -1
    + `for i <- 0 to 1 do`
      + i = 0:
        + 4 <= 8:
          + low = 0
          + `Swap(arr, i, low)`
            + **[4,8,15,16,42,23]**
    + `Swap(arr, right, low + 1)`
      + **[4,8,15,16,23,42]**
    + `return low + 1`
      + **returns 1**
    + **Note:** At this point, our list has been properly sorted. THe rest of the logic now reflects how this function ends.

+ **FOURTH RECURSION**
+ Line 6, `QuickSort(arr, left, position - 1)`: quicksort([4,8,15,16,23,42], 0, 0):
  + **left = 0**
  + **right = 0**
  + 0 can't be less than 0 so this function ends.
+ This trend will continue, with each recursion eventually ending with no further alterations to the list being made.
+ The last thing required for this code would be a return statement, or else the user would have to manually print the return of the function.
