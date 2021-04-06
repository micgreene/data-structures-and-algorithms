'use strict';

//3rd party depends
const Stack = require('./classes/stack.js');

let brackStak = new Stack();

//input: {,[,(,),],}
function multiBracketValidation(input){
  let stringArray = input.split('');

  for(let i = 0; i < stringArray.length; i++){
    brackStak.push();
  }
}
