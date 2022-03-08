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

1. The first line of code,
