'use strict';

const Node = require('./node.js');

class Queue {
  constructor() {
    this.front = null;
    this.back = null;
    this.storage = new Array();
  }

  enqueue(item) {
    let node = new Node(item);

    this.storage.push(node.value);
    if (this.storage.length === 1) {
      this.front = node;
      this.rear = node;
    } else{
      this.rear = node;
    }
  }

  dequeue() {
    if (this.storage.length < 1) {
      return 'Empty Queue!';
    }

    //assigns item as first item in the array to dequeue
    let node = this.storage.shift();

    //if we removed the last item, reset all properties to null
    if (this.storage.length < 1) {
      this.front = null;
      this.rear = null;
    }
    //if not, then we'll set the front and rear to their actual positions in the array
    else {
      this.front = this.storage[0];
      this.rear = this.storage[this.storage.length - 1];
    }
    return node;
  }

  peek(){
    if(this.storage.length < 1){
      return 'Empty Queue!';
    } else{
      return this.front;
    }
  }

  isEmpty(){
    let empty = true;
    if(!this.front){
      return empty;
    } else {
      empty = false;
      return empty;
    }
  }
}

module.exports = Queue;
