'use strict';

const Animal = require('./animal.js');

class AnimalShelter {
  constructor() {
    this.front = null;
    this.back = null;
    this.storage = new Array();
  }

  enqueue(animal) {
    let newAnimal = new Animal(animal.name, animal.animal);

    this.storage.push(newAnimal);
    if (this.storage.length === 1) {
      this.front = newAnimal;
      this.rear = newAnimal;
    } else {
      this.rear = newAnimal;
    }
  }

  dequeue(pref) {
    if (this.storage.length < 1) {
      return 'The Shelter is Empty!';
    }

    let index = 0;
    let retAnimal = null;

    if(!pref){
      retAnimal = this.storage.shift();
      return retAnimal;
    }

    while (this.storage[index] !== null) {

      if (this.storage[index].animal === pref) {
        retAnimal = this.storage.splice(index, 1);
        //if we removed the last item, reset all properties to null
        if (this.storage.length < 1) {
          this.front = null;
          this.rear = null;
        }
        //if not, then we'll set the front and rear to their actual positions in the array
        else {
          this.front = this.storage[0];
          this.rear = this.storage[this.storage.length - 1];
        }
        return retAnimal;
      } else {
        index++;
      }
    }
  }

  peek() {
    if (this.storage.length < 1) {
      return 'The Shelter is Empty!';
    } else {
      return this.front;
    }
  }

  isEmpty() {
    let empty = true;
    if (!this.front) {
      return empty;
    } else {
      empty = false;
      return empty;
    }
  }
}

module.exports = AnimalShelter;
