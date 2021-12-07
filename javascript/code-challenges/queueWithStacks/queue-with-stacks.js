'use strict';

let PseudoQueue = require('./classes/pseudoqueue-class.js');
let pseudoQ = new PseudoQueue();

pseudoQ.enqueue(1);
pseudoQ.enqueue(2);
pseudoQ.enqueue(3);
pseudoQ.dequeue();
console.log(pseudoQ.inStack);
