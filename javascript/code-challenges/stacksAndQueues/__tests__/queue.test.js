'use strict';

const { it, expect, beforeEach } = require('@jest/globals');
const Queue = require('../classes/queue.js');

describe('QUEUE CLASS', () => {
  let queue = new Queue();

  //resets the queue before each test
  beforeEach(() => {
    queue = new Queue();
  });

  //case #8
  it('Can successfully enqueue into a queue', () => {
    let value = 5;
    queue.enqueue(value);
    expect(queue.front.value).toEqual(5);
  });

  //case #9
  it('Can successfully enqueue multiple values into a queue', () => {
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);

    expect(queue.storage).toEqual([1, 2, 3]);
  });

  //case #10
  it('Can successfully dequeue out of a queue the expected value', () => {
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.dequeue();

    expect(queue.storage).toEqual([2, 3]);
  });

  //case #11
  it('Can successfully peek into a queue, seeing the expected value', () => {
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    expect(queue.peek().value).toEqual(1);
  });

  //case #12
  it('Can successfully empty a queue after multiple dequeues', () => {
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.dequeue();
    queue.dequeue();
    queue.dequeue();

    expect(queue.front).toEqual(null);
  });

  //case #13
  it('Can successfully instantiate an empty queue', () => {
    expect(queue).toEqual({ 'back': null, 'front': null, 'storage': [] });
  });

  //case #14
  it('Calling dequeue or peek on empty queue raises exception', () => {
    expect(queue.peek() || queue.dequeue()).toEqual('Empty Queue!');
  });
});
