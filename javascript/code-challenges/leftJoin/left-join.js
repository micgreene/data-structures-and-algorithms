'use strict';

const HashMap = require('./hashtable.js');

let leftMap = new HashMap(10);
let rightMap = new HashMap(10);

leftMap.set('fond', 'enamored');
leftMap.set('wrath', 'anger');
leftMap.set('diligent', 'employed');
leftMap.set('outfit', 'garb');
leftMap.set('guide', 'usher');

rightMap.set('fond', 'averse');
rightMap.set('wrath', 'delight');
rightMap.set('diligent', 'idle');
rightMap.set('guide', 'follow');
rightMap.set('flow', 'jam');

console.log(leftjoin(leftMap, rightMap));


//function takes 2 hasmaps as aparameters, compares all values and adds all values with similar keys to the "left" hash map under the same keys. All values not matching keys in the Left hashmap are ignored.
//returns value of new Left hashmap
function leftjoin(hMapLeft, hMapRight) {
  //creates a return object assigned as the left hash map
  let retMap = hMapLeft;

  //maps through the new instance of the left hashmap
  retMap = retMap.map.map((val, idx) => {

    //checks to see if the current value is undefined
    if (val) {
      //creates a reference to the key of the head node in the current element
      let currLeftKey = Object.keys(val.head.value);

      //in each of the elements of the right hashmap
      hMapRight.map.forEach(element => {

        //first check if the current element is undefined
        if (element) {
          //assigns a temporary node to track which node in the linked list we are checking
          let currNode = element.head;

          //will continue to check the linked list of the current element until the end
          while (currNode !== null) {

            //creates a reference to the key of the current node in the current element
            let currRightKey = Object.keys(currNode.value);

            //if the two current keys match then add the right hashmaps value to the left's in the same key
            if(currLeftKey[0] === currRightKey[0]){
              val.head.value[currLeftKey] += ', ' + currNode.value[currLeftKey];
            }

            //assigns currNode as the next node object in the linked list
            currNode = currNode.next;
          }
        }
      });

      //return the new ammended value
      return val;
    }
  });

  //return a new hash map
  return retMap;
}
