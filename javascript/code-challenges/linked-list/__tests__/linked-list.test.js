'use strict';

// Require our linked list implementation
const LinkedList = require('../lib/linked-list.js');

describe('Linked List', () => {
  it('should create an empty list on instantiation', () => {
    let list = new LinkedList();
    expect(list.head).toEqual(null);
  });

  it('should add new items to linked list', ()=>{
    let list = new LinkedList();
    let firstVal = 'first';
    let secVal = 'second';

    list.append(firstVal);
    expect(list.head.value).toBeEqual(firstVal);

    list.append(secVal);
    expect(list.head.next.value).toBeEqual(secVal);

  });
});
