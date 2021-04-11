'use strict';

const Tree = require('./classes/binary-search-tree.js');

let tree = new Tree();

tree.add(4);
tree.add(6);
tree.add(2);
tree.add(3);
tree.add(1);
tree.add(5);
tree.add(7);

console.log('Binary Tree Pre-Ordered: ', JSON.stringify(tree.preOrder()));

console.log('Binary Tree In-Ordered: ', JSON.stringify(tree.inOrder()));

console.log('Binary Tree Post-Ordered: ', JSON.stringify(tree.postOrder()));

let searchVal = 6;

console.log(`Does tree contain a ${searchVal}? `, tree.contains(searchVal));
