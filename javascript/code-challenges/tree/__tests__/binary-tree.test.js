'use strict';

const Node = require('../classes/node.js');
const Tree = require('../classes/binary-tree.js');

describe('TESTS FOR BINARY TREE CLASS', ()=>{
 const tree;

 beforeAll(()=>{
   const nine = new Node(9);
   const four = new Node(4);
   const three = new Node(3);
   const six = new Node(6);
   const twelve = new Node(12);
   const eleven = new Node(11);
   const twentyTwo = new Node(22);

   tree.root = nine;

   nine.left = 4;

   console.log(JSON.stringify(tree, undefined, 2));
 });
})
