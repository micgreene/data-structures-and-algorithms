'use strict';

//function takes in 2 parameters:
//1) arr: a sorted array
//2) key: a search key
//returns the index of the array’s element that is equal to the search key, or -1 if the element does not exist.
//utilizes a binary search algorithm for sake of efficiency
function binarySearch(arr, key) {
  //a represents the first index to be searched
  let a = 0;
  //b represents the last index to be searched(starting with the last index of the array)
  let b = arr.length - 1;

  //while the starting index position has not yet reached the end of the list...
  while (a <= b) {
    //m represents the current midpoint index(m) of the given array
    let m = Math.floor((a + b) / 2);

     //- ...check to see if the search key is greater or lesser than the object at the current midpoint index(m) of the search range...

     //  - ...if the number at (m) matches the search key, return the index.
    if (key === arr[m]) {
      return m;
      //  - ...if the number at (m) is greater than the search key, assign b as one index position less than the current midpoint to change the search range to the first half of the searched index section.
    } else if (key < arr[m]) {
      b = m - 1;
      //  - ...if the number at (m) is lesser than the search key, assign b as one index position more than the current midpoint to change the search range to the latter half of the searched index section.
    } else if (key > arr[m]) {
      a = m + 1;
    }
  }
  // if no matching number is found or the array contains no objects
  return -1;
}
