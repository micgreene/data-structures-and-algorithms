'use strict';

//pull in the Node Class --> this will give us the ability to instantiate new nodes to our linked list
const Node = require('./node.js');

//class defining methods and properties of LinkedList
class LinkedList {
  constructor() {
    this.head = null;
  }

  //input: any given value
  //output: the updated linked list
  //adds a new node with that value to 'tail' of the list
  append(value) {
    let node = new Node(value);

    if (!this.head) {
      this.head = node;
    } else {
      let current = this.head;

      while (current.next) {
        current = current.next;
      }
      current.next = node;
    }
    return this;
  }

  //input: any given value
  //output: none
  //adds a new node with that value to the 'head' of the list
  insert(value) {
    let node = new Node(value);

    if (!this.head) {
      this.head = node;
    } else {
      let tempLinkedList = this.head;

      this.head = node;
      this.head.next = tempLinkedList;
    }
  }

  insertbefore(searchVal, newVal) {
    let currNode = this.head;
    let prevNode = new Node(null);
    let node = new Node(newVal);

    if (!this.head) {
      this.head = node;
    } else {
      while (currNode.next) {
        if (currNode.value === searchVal) {
          if (prevNode.value === null) {
            this.head = node;
            this.head.next = currNode;
          } else {
            prevNode.next = node;
            node.next = currNode;
          }
        }
        prevNode = currNode;
        currNode = currNode.next;
      }
    }
  }

  insertafter(searchVal, newVal) {
    let currNode = this.head;
    let node = new Node(newVal);

    if (!this.head) {
      this.head = node;
    } else {
      while (currNode.next) {
        if (currNode.value === searchVal) {
          node.next = currNode.next;
          currNode.next = node;
        }
        currNode = currNode.next;
      }
    }
  }

  //input: any given value
  //output: a boolean result
  //returns a value depending on whether the input value exists as a Node’s value somewhere within the list or not
  includes(value) {
    let node = new Node(value);

    if (!this.head) {
      return false;
    } else {
      let current = this.head;

      while (node.value !== current.value && current.next) {
        current = current.next;

        if (node.value === current.value) {
          return true;
        }
      }
      return false;
    }
  }

  //input: none
  //output: a string
  //takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
  //"{ a } -> { b } -> { c } -> NULL"
  toString() {
    let stringVal = '';

    if (!this.head) {
      stringVal = '{null}';
    } else {
      stringVal += `{${this.head.value}}`;
      let current = this.head;

      while (current.next) {
        stringVal += ` -> {${current.next.value}}`;
        current = current.next;
      }
      stringVal += ' -> NULL';
    }
    return stringVal;
  }
}

module.exports = LinkedList;


