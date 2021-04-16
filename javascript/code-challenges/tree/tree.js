'use strict';

const Tree = require('./classes/binary-search-tree.js');
const MaxValTree = require('./classes/binary-tree-max-value.js');

let tree = new Tree();
let maxValTree = new MaxValTree();

tree.add(5);
tree.add(4);
tree.add(7);
tree.add(3);
tree.add(5);
tree.add(6);
tree.add(8);

maxValTree.add(5);
maxValTree.add(4);
maxValTree.add(7);
maxValTree.add(3);
maxValTree.add(5);
maxValTree.add(6);
maxValTree.add(8);

console.log('Binary Tree Pre-Ordered: ', JSON.stringify(tree.preOrder()));

console.log('Binary Tree In-Ordered: ', JSON.stringify(tree.inOrder()));

console.log('Binary Tree Post-Ordered: ', JSON.stringify(tree.postOrder()));

let searchVal = 6;

console.log(`Does tree contain a ${searchVal}? `, tree.contains(searchVal));

searchVal = 7;

console.log(`Does tree contain a ${searchVal}? `, tree.contains(searchVal));

console.log('Tree1: ', JSON.stringify(tree));
console.log('Breadth First: ', tree.breadthFirst());

console.log('Max Value Tree: ', JSON.stringify(maxValTree));
console.log('Max Value: ', maxValTree.findMaximumValue());
