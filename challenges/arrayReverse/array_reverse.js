'use strict';

function reverseArray(arr){
  let startIndx = 0;
  let endIndx = arr.length - 1;

  while (startIndx <= endIndx) {
    let tmp = startVal;
    arr[startIndx] = arr[endIndx];
    arr[endIndx] = tmp;
    startIndx++;
    endIndx--;
  }
}
