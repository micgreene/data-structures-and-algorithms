'use strict';

const Animal = require('../classes/animal.js');
const Queue = require('../classes/animal-shelter.js');

describe('QUEUE CLASS TESTS', ()=>{
  //create an instance of the queue class to test
  let queue = new Queue();
  
  //make a bunch of animals of different types
  let fluffy = new Animal('Fluffy', 'cat');
  let coco = new Animal('Coco', 'dog');
  let rover = new Animal('Rover', 'dog');
  let mr_Kayden = new Animal('Mr Kayden', 'cat');
  let spot = new Animal('Spot', 'dog');

  //resets the queue for each test
  beforeEach(()=>{
    queue = new Queue();
  });

  //test case #1
  it('.enqueue(animal) should add a new animal to the queue\'s internal storage', ()=>{
    //send some buddies to the shelter
    queue.enqueue(fluffy);
    queue.enqueue(spot);
    queue.enqueue(mr_Kayden);

    expect(queue.storage).toEqual([{'animal': 'cat', 'name': 'Fluffy'}, {'animal': 'dog', 'name': 'Spot'}, {'animal': 'cat', 'name': 'Mr Kayden'}]);
  });

  //test case #2
  it('.dequeue(pref) should return the animal of the type pref that has been in the "shelter" (internal storage) the longest', ()=>{
    //send some buddies to the shelter
    queue.enqueue(mr_Kayden);
    queue.enqueue(rover);
    queue.enqueue(coco);

    expect(queue.dequeue('dog')).toEqual([{'animal': 'dog', 'name': 'Rover'}]);
    expect(queue.dequeue('cat')).toEqual([{'animal': 'cat', 'name': 'Mr Kayden'}]);
  });

  //test case #3
  it('if .dequeue() is not given a pref, return the poor baby (animal) who has been there (internal storage) the longest', ()=>{
    //send some buddies to the shelter
    queue.enqueue(spot);
    queue.enqueue(coco);
    queue.enqueue(fluffy);
    queue.enqueue(rover);
    queue.enqueue(mr_Kayden);

    expect(queue.dequeue()).toEqual({'animal': 'dog', 'name': 'Spot'});
  });
});
