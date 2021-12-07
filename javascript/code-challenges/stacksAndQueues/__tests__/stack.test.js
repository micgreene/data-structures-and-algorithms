'use strict';

const { it, expect, beforeEach } = require('@jest/globals');
const Stack = require('../classes/stack.js');

describe('STACK CLASS', () => {
  let stack = new Stack();

  //resets the stack for each test
  beforeEach(() => {
    stack = new Stack();
  });

  //case #1
  it('Can successfully push onto a stack', () => {
    let value = 5;
    stack.push(value);
    expect(stack.top).toEqual(5);
  });

  //case #2
  it('Can successfully push multiple values onto a stack', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);
    expect(stack.storage).toEqual([1, 2, 3]);
  });

  //case #3
  it('Can successfully pop off the stack', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.pop();

    expect(stack.storage).toEqual([1, 2]);
  });

  //case #4
  it('Can successfully empty a stack after multiple pops', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();

    expect(stack.top).toEqual(null);
  });

  //case #5
  it('Can successfully peek the next item on the stack', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);

    expect(stack.peek()).toEqual(3);
  });

  //case #6
  it('Can successfully instantiate an empty stack', () => {
    expect(stack).toEqual(
      {
        'storage': [],
        'top': null,
      }
    );
  });

  //case #7
  it('Calling pop or peek on empty stack raises exception', () => {
    expect(stack.pop() || stack.peek()).toEqual('Stack Empty!');
  });
});
