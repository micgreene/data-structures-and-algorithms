'use strict';

//internal modules
const Animal = require('./classes/animal.js');
const Queue = require('./classes/animal-shelter.js');

//make an empty queue to test
let testQueue = new Queue();

//make a bunch of animals of different types
let fluffy = new Animal('Fluffy', 'cat');
let coco = new Animal('Coco', 'dog');
let rover = new Animal('Rover', 'dog');
let mr_Kayden = new Animal('Mr Kayden', 'cat');
let spot = new Animal('Spot', 'dog');

testQueue.enqueue(fluffy);
testQueue.enqueue(coco);
testQueue.enqueue(mr_Kayden);


console.log('The dequeue return: ', testQueue.dequeue());

console.log('The final storage: ', testQueue.storage);
