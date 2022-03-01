# Insertion Sort

## Introduction

**In this article we will review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample list.**

**I will then show the step-by-step output after each iteration.**

## Pseudocode

**Line #**
1- `InsertionSort(int[] arr)`
2-  `FOR i = 1 to arr.length`
3-    `int j <-- i - 1`
4-    `int temp <-- arr[i]`
5-    `WHILE j >= 0 AND temp < arr[j]`
6-      `arr[j + 1] <-- arr[j]`
7-      `j <-- j - 1`
8-    `arr[j + 1] <-- temp`

### Algorithm

*For this example, we will use a sample list:*
**[8,4,23,42,16,15]**

1. The first line of code, `InsertionSort(int[] arr)`, is telling us that this is a function.

+ The function is going to have a parameter of a list ("arr" or *"array"*) that is comprised of integers ("int[]").

1. Line 2, `FOR i = 1 to arr.length`, starts a *for loop* where i begins as 1 and is incemented until it equals the length of the given list.

+ *Since we don't want to go out of the index of the list, in this case we will use the range() function in Python which will only iterate to one integer shy of the list length.*
  + **arr.length = 6, so range(1,6)**

+ Below we will now iterate through the function as each value of i:
  + **i = 1**:
    + Line 3, `int j <-- i - 1`, creates a new variable, j, as one index in position less than i. j will act as a comparison to the prior index in the list.
      + **j = 0**
    + Line 4, `int temp <-- arr[i]`, stores the current index in the list being compared as a temporary variable.
      + **temp = 4**
    + Line 5, `WHILE j >= 0 AND temp < arr[j]`, starts a *while loop* that continues as long as j is greater than or equal to 0, *and* the temporary value of the current index being compared is less than its previous index.
      + Here is where the bulk of the "sorting" takes place.
        + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list. This is because the while loop is searching for integers that are larger than the integers in the previous indexes.
          + **arr[1] = 8**
          + *sample_list = [8,8,23,42,16,15]*
        + Line 7, `j <-- j - 1`, decrements j by 1.
          + **j = -1**
        + Now since `j == -1` we exit the while loop.
    + j was decremented so on Line 8, `arr[j + 1] <-- temp`, we can swap the temp value in the index prior to the last one we moved in our while loop.
      + **arr[0] = 4**
    + *sample_list = [4,8,23,42,16,15]*
  + **i = 2**:
    + Line 3, `int j <-- i - 1`, creates a new variable, j, as one index in position less than i. j will act as a comparison to the prior index in the list.
      + **j = 1**
    + Line 4, `int temp <-- arr[i]`, stores the current index in the list being compared as a temporary variable.
      + **temp = 23**
    + Line 5, `WHILE j >= 0 AND temp < arr[j]`, sees that temp(23) is not less than arr[1](8) and exits the while loop.
    + j was not decremented so on Line 8, `arr[j + 1] <-- temp`, we leave the current index as the same value.
      + **arr[2] = 23**
      + *sample_list = [4,8,23,42,16,15]*
  + **i = 3**:
    + Line 3, `int j <-- i - 1`, creates a new variable, j, as one index in position less than i. j will act as a comparison to the prior index in the list.
      + **j = 2**
    + Line 4, `int temp <-- arr[i]`, stores the current index in the list being compared as a temporary variable.
      + **temp = 42**
    + Line 5, `WHILE j >= 0 AND temp < arr[j]`, sees that temp(42) is not less than arr[2](23) and exits the while loop.
    + j was not decremented so on Line 8, `arr[j + 1] <-- temp`, we leave the current index as the same value.
      + **arr[3] = 42**
      + *sample_list = [4,8,23,42,16,15]*
  + **i = 4**:
    + Line 3, `int j <-- i - 1`, creates a new variable, j, as one index in position less than i. j will act as a comparison to the prior index in the list.
      + **j = 3**
    + Line 4, `int temp <-- arr[i]`, stores the current index in the list being compared as a temporary variable.
      + **temp = 16**
    + Line 5, `WHILE j >= 0 AND temp < arr[j]`, starts a *while loop* that continues as long as j is greater than or equal to 0, *and* the temporary value of the current index being compared is less than its previous index.
      + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list. This is because the while loop is searching for integers that are larger than the integers in the previous indexes.
        + **arr[4] = 42**
        + *sample_list = [8,8,23,42,42,15]*
      + Line 7, `j <-- j - 1`, decrements j by 1.
        + **j = 2**
      + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list again.
        + **arr[3] = 23**
        + *sample_list = [8,8,23,23,42,15]*
      + Line 7, `j <-- j - 1`, decrements j by 1.
        + **j = 1**
      + Line 5, `WHILE j >= 0 AND temp < arr[j]`, sees that temp(16) is not less than arr[1](8) and exits the while loop.
    + j was decremented, so on Line 8, `arr[j + 1] <-- temp`, we can swap the temp value in the index prior to the last one we moved in our while loop.
      + **arr[2] = 16**
      + *sample_list = [4,8,16,23,42,15]*
  + **i = 5**:
    + Line 3, `int j <-- i - 1`, creates a new variable, j, as one index in position less than i. j will act as a comparison to the prior index in the list.
      + **j = 4**
    + Line 4, `int temp <-- arr[i]`, stores the current index in the list being compared as a temporary variable.
      + **temp = 15**
    + Line 5, `WHILE j >= 0 AND temp < arr[j]`, starts a *while loop* that continues as long as j is greater than or equal to 0, *and* the temporary value of the current index being compared is less than its previous index.
      + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list. This is because the while loop is searching for integers that are larger than the integers in the previous indexes.
        + **arr[5] = 42**
        + *sample_list = [4,8,16,23,42,42]*
      + Line 7, `j <-- j - 1`, decrements j by 1.
        + **j = 3**
      + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list again.
        + **arr[4] = 23**
        + *sample_list = [4,8,16,23,23,42]*
      + Line 7, `j <-- j - 1`, decrements j by 1.
        + **j = 2**
      + Line 6, `arr[j + 1] <-- arr[j]`, reassigns the current index being examined with the previous index in the list again.
        + **arr[3] = 23**
        + *sample_list = [4,8,16,16,23,42]*
      + Line 7, `j <-- j - 1`, decrements j by 1.
        + **j = 1**
      + Line 5, `WHILE j >= 0 AND temp < arr[j]`, sees that temp(15) is not less than arr[1](8) and exits the while loop.
    + j was decremented, so on Line 8, `arr[j + 1] <-- temp`, we can swap the temp value in the index prior to the last one we moved in our while loop.
      + **arr[2] = 15**
      + *sample_list = [4,8,15,16,23,42]*

1. At this point, we have reached the end of `range(1,6)` and the list has been altered in place.

+ **Note:** *This code would still require a return statement or else the user would have to manually print the function when calling it.*
