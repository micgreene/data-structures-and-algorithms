'use strict';

const Node = require('./node-class.js');

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
}

module.exports = Stack;
