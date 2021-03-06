'use strict';

const Node = require('../lib/node.js');

//creates a suite of tests
describe('NODE CLASS', () =>{
  //describes and creates individual tests
  it ('can create a new node', ()=>{
    let val = 'test value';
    let node = new Node(val);

    //assertions to check the values against the expected values created above
    expect(node.value).toEqual(val);
    expect(node.next).toBeNull();
  });
});
