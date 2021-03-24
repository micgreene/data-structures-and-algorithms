'use strict';

class Queue {
  constructor() {
    this.front = null;
    this.back = null;
    this.storage = new Array();
  }

  enqueue(item) {
    this.storage.push(item);
    if (this.storage.length === 1) {
      this.front = item;
      this.rear = item;
    } else{
      this.rear = item;
    }
  }

  dequeue() {
    if (this.storage.length < 1) {
      return 'empty queue';
    }

    //assigns item as first item in the array to dequeue
    let item = this.storage.shift();

    //if we removed the last item, reset all properties to null
    if (this.storage.length === 0) {
      this.front = null;
      this.rear = null;
    }
    //if not, then we'll set the front and rear to their actual positions in the array
    else {
      this.front = this.storage[0];
      this.rear = this.storage[this.storage.length - 1];
    }
    return item;
  }


}

module.exports = Queue;
