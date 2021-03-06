'use strict';

const { it, expect, beforeEach } = require('@jest/globals');

// Require our linked list implementation
const LinkedList = require('../lib/linked-list.js');

//suite of tests for LinkedList.js
describe('Linked List', () => {
  let list = new LinkedList();
  //resets the list object as a new LinkedList between each test
  beforeEach(() => {
    list = new LinkedList();
  });

  //test cases (6 total)
  it('should create an empty list on instantiation', () => {
    expect(list.head).toEqual(null);
  });

  it('should add new items to linked list', ()=>{
    let firstVal = 'first';
    let secVal = 'second';

    list.append(firstVal);
    expect(list.head.value).toEqual(firstVal);

    list.append(secVal);
    expect(list.head.next.value).toEqual(secVal);
  });

  it('"insert(value)" should add a newly inserted value as the "head" of the linked list, head will properly point to the first node', ()=>{
    let oldHead = 'old';
    let newHead = 'new';

    list.insert(oldHead);
    expect(list.head.value).toEqual(oldHead);
    list.insert(newHead);
    expect(list.head.value).toEqual(newHead);
  });

  it('Can properly insert multiple nodes into the linked list', ()=>{
    list.append(4);
    list.append(5);
    list.append(6);

    expect(list.head.value).toEqual(4);
    expect(list.head.next.value).toEqual(5);
    expect(list.head.next.next.value).toEqual(6);
  });

  it('"includes(value)" should take any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list', ()=>{
    //creates a Linked List of:
    //'{1} -> {2} -> {3} -> NULL'
    list.append(1);
    list.append(2);
    list.append(3);
    let testCase1 = list.includes(3);
    let testCase2 = list.includes(4);

    expect(testCase1).toEqual(true);
    expect(testCase2).toEqual(false);
  });

  it('"toString()" should return a string representing all the values in the Linked List, formatted as: { a } -> { b } -> { c } -> NULL', ()=>{
    list.append(1);
    list.append(2);
    list.append(3);
    let testCase = list.toString();

    expect(testCase).toEqual('{1} -> {2} -> {3} -> NULL');
  });
});
