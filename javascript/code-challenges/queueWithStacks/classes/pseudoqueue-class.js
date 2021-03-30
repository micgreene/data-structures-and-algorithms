'use strict';

const Node = require('./node-class.js');
const Stack = require('./stack-class.js');

class PseudoQueue {
  constructor() {
    this.inStack = new Stack();
    this.outStack = new Stack();
    this.front = null;
    this.rear = null;
  }

  enqueue(value) {
    let node = new Node(value);

    this.inStack.push(node);

    if (this.inStack.storage.length === 1) {
      this.front = node;
      this.rear = node;
    } else {
      this.rear = node;
    }
  }

  dequeue() {
    if (this.inStack.peek() === 'Stack Empty!') {
      return 'Stack Empty!';
    } else {
      while (this.inStack.peek() !== 'Stack Empty!') {
        this.outStack.push(this.inStack.pop());
      }

      let dequeued = this.outStack.pop();

      while(this.outStack.peek() !== 'Stack Empty!'){
        this.inStack.push(this.outStack.pop());
      }
      return dequeued;
    }
  }
}
module.exports = PseudoQueue;
