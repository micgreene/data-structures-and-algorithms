'use strict';

const LinkedList = require('./linked-list.js');

class HashMap{
  //to avoid collisions:
  //create a new hashtable of *2 size
  //for each thing in old hash table, do a .set() to the  new table
  //delete old hash table
  constructor(size){
    this.size = size;
    this.map = new Array(size).fill();
  }

  hash(key){
    let hashSum = key.split('').reduce( (acc, val) =>{
      let cc = val.charCodeAt(0);
      let num = acc + cc;
      return num;

    }, 0);

    let hash = hashSum * 599 % this.size;

    return hash;
  }

  set(key, value){
    let hash = this.hash(key);// should return a number of the index

    if( !this.map[hash] ){
      this.map[hash] = new LinkedList();
    }

    let entry = {[key]: value};

    this.map[hash].append(entry);
  }

  get(key){
    //1-hash the key
    let hash = this.hash(key);// should return a number of the index

    //if linked list is empty then return null
    if(this.map[hash] === undefined){
      return null;
    }

    //2 - get value of this.map[hash]
    let currNode = this.map[hash].head;

    //3-traverse the linked list and fimd the actual one (collisions means there is more than one)
    while(currNode !== null){
      if(key === Object.keys(currNode.value)[0]){

        //4 - return that value
        return currNode.value[key];
      }

      currNode = currNode.next;
    }

    return null;
  }

  contains(key){
    //1-hash the key
    let hash = this.hash(key);// should return a number of the index

    //if linked list is empty then return false
    if(this.map[hash] === undefined){
      return false;
    }

    //2 - get value of this.map[hash]
    let currNode = this.map[hash].head;

    //3-traverse the linked list and fimd the actual one (collisions means there is more than one)
    while(currNode !== null){
      if(key === Object.keys(currNode.value)[0]){

        //4 - return true if found
        return true;
      }

      currNode = currNode.next;
    }

    //4 - return false if not
    return false;
  }
}

// let testMap = new HashMap(10);


// testMap.set('Mike', 'O.G.');
// testMap.set('Willson', 'Mr. Smiley');
// testMap.set('Terry', 'Turbo');
// testMap.set('Darren', 'Dare-Bear');
// testMap.set('Manolio', 'The Professor.');

// console.log('Hash Table feat. MKG: ', JSON.stringify(testMap.map), '\n');
// console.log('yes Get Method: ', testMap.get('Mike'));
// console.log('no Get Method: ', testMap.get('Bobby'));
// console.log('yes Has Method: ', testMap.has('Mike'));
// console.log('no Has Method: ', testMap.has('Bobby'));
// console.log('hashed value: ', testMap.hash('Mike'));

module.exports = HashMap;
