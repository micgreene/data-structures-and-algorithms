'use strict';

const HashMap = require('../hashtable.js');

describe('should create a hashtable which utilizes hash(), set(), get(), and has() methods', () => {
  let hashMap = new HashMap(10);
  beforeEach(()=>{
    hashMap = new HashMap(10);
  });

  //case #1 - Creates a Hash Map
  it('Can create a new, empty Hash Map', () => {
    expect(hashMap.map.length).toEqual(10);
  });

  //case #2 - .Set() Method - Add a New Key:Value Pair
  it('Adding a key/value to your hashtable results in the value being in the data structure', () => {
    hashMap.set('Mike', 'O.G.');

    expect(JSON.stringify(hashMap.map)).toEqual(`[{"head":{"value":{"Mike":"O.G."},"next":null}},null,null,null,null,null,null,null,null,null]`);
  });

  //case #3 - .Get() Method - List Contains Item
  it('Retrieving based on a key returns the value stored', () => {
    hashMap.set('Mike', 'O.G.');

    expect(hashMap.get('Mike')).toEqual('O.G.');
  });

  //case #4 - .Get() Method - List Doesn't Contain Item
  it('Successfully returns null for a key that does not exist in the hashtable', () => {
    hashMap.set('Mike', 'O.G.');

    expect(hashMap.get('Frankie Walnuts')).toEqual(null);
  });

  //case #5 - .Set() Method - Assign two Keys to One Bucket
  it('Successfully handle a collision within the hashtable', () => {
    hashMap.set('Willson', 'Mr. Smiley');
    hashMap.set('Terry', 'Turbo');
    hashMap.set('Darren', 'Dare-Bear');

    expect(JSON.stringify(hashMap.map)).toEqual(`[null,null,null,null,null,null,{"head":{"value":{"Willson":"Mr. Smiley"},"next":{"value":{"Terry":"Turbo"},"next":{"value":{"Darren":"Dare-Bear"},"next":null}}}},null,null,null]`);
  });

  //case #6 - .Get() Method - With Collision
  it('Successfully retrieve a value from a bucket within the hashtable that has a collision', () => {
    hashMap.set('Willson', 'Mr. Smiley');
    hashMap.set('Terry', 'Turbo');
    hashMap.set('Darren', 'Dare-Bear');

    expect(hashMap.get('Terry')).toEqual('Turbo');
  });

  //case #7 - .Hash() Method - Hashing a Key
  it('Successfully hash a key to an in-range value', () => {

    expect(hashMap.hash('Mike')).toEqual(0);
  });
});
