'use strict';

const KTree = require('./classes/k-tree.js');
const Node = require('./classes/node.js');

let kTree = new KTree();
let rootNode = new Node(1);
let childNode1 = new Node(2);
let childNode2 = new Node(3);
let childNode3 = new Node(4);
let childNode4 = new Node(5);
let childNode5 = new Node(6);
let childNode6 = new Node(15);

kTree.root = rootNode;
kTree.root.children.push(childNode1, childNode2, childNode3);
kTree.root.children[1].children.push(childNode4, childNode5, childNode6);

function fizzBuzzTree(tree) {
  if (!tree.root) {
    return 'Empty Tree!';
  }

  let retTree = new KTree();
  let height = 0;
  let nodes = [];
  let queue = [];

  queue.push(tree.root);

  while (queue.length > 0) {
    let currentNode = queue.shift();

    if (currentNode.value % 3 === 0 && currentNode.value % 5 !== 0) {
      currentNode.value = ('Fizz');
    } else if (currentNode.value % 3 !== 0 && currentNode.value % 5 === 0) {
      currentNode.value = ('Buzz');
    } else if (currentNode.value % 3 === 0 && currentNode.value % 5 === 0) {
      currentNode.value = ('FizzBuzz');
    }

    if (currentNode.children.length > 0) {
      for (let i = 0; i < currentNode.children.length; i++) {
        queue.push(currentNode.children[i]);
      }
    }
  }
  return JSON.stringify(tree);
}

console.log(fizzBuzzTree(kTree));
