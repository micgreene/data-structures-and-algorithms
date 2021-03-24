'use strict';

const Node = require('./node.js');

class Stack {
  constructor() {
    this.top = null;
    this.storage = new Array();
  }


  push(item) {
    let node = new Node(item);
    this.storage.push(node.value);
    this.top = node.value;
  }

  pop() {
    if (this.storage.length < 1) {
      this.top = null;
      
      return 'Stack Empty!';
    } else {
      let node = this.storage.pop();
      console.log(this.storage);
      return node;
    }
  }

  peek() {
    if (this.storage.length < 1) {
      return 'Stack Empty!';
    } else {
      return this.top;
    }
  }

  isEmpty(){
    let empty = true;
    if (this.storage.length < 1) {
      return empty;
    } else {
      empty = false;
      return empty;
    }
  }
}

module.exports = Stack;
