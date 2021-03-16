'use strict';

//const { it, expect, beforeEach } = require('@jest/globals');

// Require our linked list implementation
const LinkedList = require('../../linked-list/lib/linked-list.js');
const zipList = require('../ll-zip.js');

//suite of tests for LinkedList.js
describe('Linked List', () => {
  let list = new LinkedList();
  let list2 = new LinkedList();
  //resets the list object as a new LinkedList between each test
  beforeEach(() => {
    list = new LinkedList();
    list2 = new LinkedList();
  });

  //test cases (6 total)
  it('should create a reference to the head of the zipped list', () => {
    list.append(1);
    list.append(2);
    list.append(3);

    list2.append(4);
    list2.append(5);
    list2.append(6);

    let testcase1 = zipList(list, list2);

    expect(testcase1.head.value).toEqual(1);
  });

  it('should zip together two singly linked lists', ()=>{
    list.append(1);
    list.append(3);

    list2.append(2);
    list2.append(4);

    let testcase2 = zipList(list, list2);

    expect(testcase2.head.value).toEqual(1);
    expect(testcase2.head.next.value).toEqual(2);
    expect(testcase2.head.next.next.value).toEqual(3);
    expect(testcase2.head.next.next.next.value).toEqual(4);
  });

  it('should return null if link lists are both empty', ()=>{
    let testcase3 = zipList(list, list2);

    expect(testcase3.head).toEqual(null);
  });

  it('should return the contents of one list if the other is empty', ()=>{
    list.append(4);
    list.append(5);
    list.append(6);

    let testcase4 = zipList(list, list2);

    expect(testcase4.head.value).toEqual(4);
    expect(testcase4.head.next.value).toEqual(5);
    expect(testcase4.head.next.next.value).toEqual(6);
  });
});
