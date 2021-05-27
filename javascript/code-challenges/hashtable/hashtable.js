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

  get(){
    //1-hash the key
    //2 - get value of this.map[hash]
    //3-traverse the linked list and fimd the actual one (collisions means there is more than one)
    //4 - return that value

  }

  has(){
    //1-hash the key
    //2 - get value of this.map[hash]
    //3-traverse the linked list and fimd the actual one (collisions means there is more than one)
    //4 - return true or false
  }
}

let testMap = new HashMap();

console.log('empty hash map: ', testMap);

testMap.set('Mike', 'O.G.');

console.log('Hash Table feat. MKG: ', testMap);
module.exports = HashMap;
