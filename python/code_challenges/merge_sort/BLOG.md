# Insertion Sort

**Author: Michael Greene**

## Introduction

**In this article we will review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample list.**

**I will then show the step-by-step output after each iteration.**

## Pseudocode

**Line #**
1-   `ALGORITHM Mergesort(arr)`
2-       `DECLARE n <-- arr.length`
3-      `if n > 1`
4-        `DECLARE mid <-- n/2`
5-        `DECLARE left <-- arr[0...mid]`
6-        `DECLARE right <-- arr[mid...n]`
7-        `// sort the left side`
8-        `Mergesort(left)`
9-        `// sort the right side`
10-        `Mergesort(right)`
11-        `// merge the sorted left and right sides together`
12-        `Merge(left, right, arr)`
13-  `ALGORITHM Merge(left, right, arr)`
14-      `DECLARE i <-- 0`
15-      `DECLARE j <-- 0`
16-      `DECLARE k <-- 0`
17-      `while i < left.length && j < right.length`
18-          `if left[i] <= right[j]`
19-              `arr[k] <-- left[i]`
20-              `i <-- i + 1`
21-          `else`
22-              `arr[k] <-- right[j]`
23-              `j <-- j + 1`
24-          `k <-- k + 1`
25-      `if i = left.length`
26-         `set remaining entries in arr to remaining values in right`
27-      `else`
28-         `set remaining entries in arr to remaining values in left`

### Algorithm

*For this example, we will use a sample list:*
**[8,4,23,42,16,15]**

1. The first line of code, `Mergesort(arr)`, is telling us that this is a function.

+ The function is going to have a parameter of a list ("arr" or *"array"*).

1. Line 2, `n <-- arr.length`, declares a new variable, 'n', as the length of the array.

+ **n = 6**

1. Line 3, `if n > 1`, checks to see if the length of the list that has been passed in is greater than 1.

+ **6 > 1**

+ 6 is greater than 1, so:
  + Line 4, `mid <-- n/2`, declares a new variable 'mid' as half the value of n, or the "middle index", for our purposes.
  + Line 5, `left <-- arr[0...mid]` declares a new variable 'left' as a list comprised of the indexes of our passed in list from the first index up until the middle.
    + **left = [8,4,23]**
  + Line 6, `right <-- arr[mid...n]` declares a new variable 'left' as a list comprised of the indexes of our passed in list from the middle index up until the last.
    + **right = [42,16,15]**
  + #The next lines are where the sorting takes place. As this process happens recursively I will do my best to visualy track what is happening:
  + First the left side is sorted:
    + Line 8, `Mergesort(left)`, is calling the Mergesort() function again recursively, this time using the 'left' variable list we just created as the parameter.
  + Then the right side is sorted:
    + Line 10, `Mergesort(right)`, is calling the Mergesort() function again recursively, this time using the 'right' variable list we just created as the parameter.
  + Finally the two halves are sorted then merged back together:
    + Line 12, `Merge(left, right, arr)`, is calling a separate function which will now sort and remerge the lists.
      + **Note:** What this will eventually do is divide the original list up into several lists of just 2 integers each. Each list will be split into a left and right list by themselves, then sorted back into the main list. This will keep happening until all indexes have been compared to eachother.

1. Line 13, `Merge(left, right, arr)`, is telling us that this is a function.

+ The function is going to have 3 parameters:
  + left (list)
  + right (list)
  + arr (list)

1. Line 14, `i <-- 0`, declares a tracking variable 'i' as 0.

1. Line 15, `j <-- 0`, declares a tracking variable 'j' as 0.

1. Line 16, `k <-- 0`, declares a tracking variable 'k' as 0.

1. Line 17 begins a while loop, which continues as long as i is less than the length of the left list and j is less than the length of the right list.

1.
17-      `while i < left.length && j < right.length`
18-          `if left[i] <= right[j]`
19-              `arr[k] <-- left[i]`
20-              `i <-- i + 1`
21-          `else`
22-              `arr[k] <-- right[j]`
23-              `j <-- j + 1`
24-          `k <-- k + 1`
25-      `if i = left.length`
26-         `set remaining entries in arr to remaining values in right`
27-      `else`
28-         `set remaining entries in arr to remaining values in left`
