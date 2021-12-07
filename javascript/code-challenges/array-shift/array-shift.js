'use strict';

function insertShiftArray(arr, addVal) {
  let midIdx = Math.floor(arr.length / 2); // 2

  let oldVal = arr[midIdx]; // 4

  arr[midIdx] = addVal; // [1,2,3,5]

  arr.length = arr.length + 1;

  for (let i = midIdx + 1; i < arr.length; i++) {
    var storedNum = arr[i];
    if(storedNum !== null){
      arr[i] = oldVal;
      oldVal = storedNum;
    }else{
      arr[arr.length] = oldVal;
    }
  }
  return arr;
}

console.log(insertShiftArray([1,2,4,5], 3));
