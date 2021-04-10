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
        } else return false;
        break;
      case ']':
        if (brackStak.peek() !== 'Stack Empty!') {
          comparison = brackStak.pop();
          if (comparison !== '[') {
            return false;
          }
        } else return false;
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

  console.log('brackStack.storage-------->  ', brackStak.storage.length);
  if(brackStak.isEmpty() === true){
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
console.log(multiBracketValidation('test2:  ', test2));
console.log(multiBracketValidation('test3:  ', test3));
console.log(multiBracketValidation('test4:  ', test4));
console.log(multiBracketValidation('test5:  ', test5));
console.log(multiBracketValidation('test6:  ', test6));
console.log(multiBracketValidation('test7:  ', test7));
console.log(multiBracketValidation('test8:  ', test8));
console.log(multiBracketValidation('test9:  ', test9));
