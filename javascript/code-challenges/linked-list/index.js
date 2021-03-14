'use strict';

const LinkedList = require('./lib/linked-list.js');

let linkedlistobj = new LinkedList();

linkedlistobj.append(2);
linkedlistobj.append(7);
linkedlistobj.append(3);
linkedlistobj.append(4);
linkedlistobj.append(5);

linkedlistobj.kthfromend(5);

console.log(linkedlistobj);
