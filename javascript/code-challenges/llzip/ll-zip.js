'use strict';

//pull in the LinkedList ---> allows us to to create new singly linked list objects
const LinkedList = require('../linked-list/lib/linked-list.js');

//creating two lists to display function
let linklist_0bj1 = new LinkedList();
linklist_0bj1.append(1);
linklist_0bj1.append(3);
linklist_0bj1.append(5);

let linklist_0bj2 = new LinkedList();
linklist_0bj2.append(2);
linklist_0bj2.append(4);
linklist_0bj2.append(6);

//input: a singly linked list, a singly linked list
//output: a reference to the zipped list's head
//takes two singly linked lists and zips them into one with alternating nodes
function zipLists(linkli_1, linkli_2) {
  let ret_li = new LinkedList();
  let counter = 0;
  linkli_1 = linkli_1.head;
  linkli_2 = linkli_2.head;

  while (linkli_1 || linkli_2) {
    counter++;
    if (counter % 2 !== 0) {
      if (linkli_1) {
        ret_li.append(linkli_1.value);
        linkli_1 = linkli_1.next;
      } else if (linkli_2.value) {
        ret_li.append(linkli_2.value);
        linkli_2 = linkli_2.next;
      }
    } else {
      if (linkli_2) {
        ret_li.append(linkli_2.value);
        linkli_2 = linkli_2.next;
      } else if (linkli_1.value) {
        ret_li.append(linkli_1.value);
        linkli_1 = linkli_1.next;
      }
    }
  }
  return ret_li;
}

zipLists(linklist_0bj1, linklist_0bj2);

module.exports = zipLists;
