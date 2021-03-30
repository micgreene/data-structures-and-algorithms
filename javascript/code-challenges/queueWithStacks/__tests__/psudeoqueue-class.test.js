'use strict';

//3rd party dependencies
const supertest = require('supertest');

//local modules to be tested
const PseudoQueue = require('../classes/pseudoqueue-class.js');

//creates test parameters
describe('PSEUDOQUEUE CLASS TESTS', () => {
  //case #1 - Enqueue Method
  it('enqueue should return a stack structured FIFO, with the enqueue\'d value being at the rear position ', () => {
    //create new psuedoqueue object to test
    let pq = new PseudoQueue();
    pq.enqueue(1);
    pq.enqueue(2);
    pq.enqueue(3);

    expect(pq.inStack).toEqual({ 'storage': [{ 'value': 1 }, { 'value': 2 }, { 'value': 3 }], 'top': { 'value': 3 } });
  });

  //case #2 - Dequeue Method with stack of nodes
  it('dequeue should return the front of the queue, or in this case the bottom of the stack', () => {
    //create new psuedoqueue object to test
    let pq = new PseudoQueue();
    pq.enqueue(1);
    pq.enqueue(2);
    pq.enqueue(3);
    let testcase = pq.dequeue();

    expect(testcase).toEqual({ 'value': 1 });
  });

  //case #3 - Dequeue Method with empty stack
  it('dequeue should return Stack Empty! when stack is empty', () => {
    //create new psuedoqueue object to test
    let pq = new PseudoQueue();
    let testcase = pq.dequeue();

    expect(testcase).toEqual('Stack Empty!');
  });
});
