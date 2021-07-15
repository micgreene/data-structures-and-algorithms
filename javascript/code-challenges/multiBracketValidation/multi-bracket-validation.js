'use strict';

//3rd party depends
const Stack = require('./classes/stack.js');

let brackStak = new Stack();

//input: {,[,(,),],}
function multiBracketValidation(input) {
  let stringArray = input.split('');
  let comparison = null;

  for (let i = 0; i < stringArray.length; i++) {
    if (stringArray[i] === '{' || stringArray[i] === '[' || stringArray[i] === '(') {
      brackStak.push(stringArray[i]);
    }
    switch (stringArray[i]) {
      case '}':
        if (brackStak.peek() !== 'Stack Empty!') {
          comparison = brackStak.pop();
          if (comparison !== '{') {
            return false;
          }
        } //else return true;
        break;
      case ']':
        if (brackStak.peek() !== 'Stack Empty!') {
          comparison = brackStak.pop();
          if (comparison !== '[') {
            return false;
          }
        } //else return true;
        break;
      case ')':
        if (brackStak.peek() !== 'Stack Empty!') {
          comparison = brackStak.pop();
          if (comparison !== '(') {
            return false;
          }
        }
        break;
    }
  }
  if (brackStak.isEmpty() === true) {
    return true;
  } else return false;
}

let test1 = '{}(){}';
let test2 = '()[[Extra Characters]]';
let test3 = '{}{Code}[Fellows](())';
let test4 = '[({}]';
let test5 = '(](';
let test6 = '{(})';
let test7 = '{';
let test8 = ')';
let test9 = '[}';

console.log('test1:  ', multiBracketValidation(test1));
console.log('test2:  ', multiBracketValidation(test2));
console.log('test3:  ', multiBracketValidation(test3));
console.log('test4:  ', multiBracketValidation(test4));
console.log('test5:  ', multiBracketValidation(test5));
console.log('test6:  ', multiBracketValidation(test6));
console.log('test7:  ', multiBracketValidation(test7));
console.log('test8:  ', multiBracketValidation(test8));
console.log('test9:  ', multiBracketValidation(test9));
