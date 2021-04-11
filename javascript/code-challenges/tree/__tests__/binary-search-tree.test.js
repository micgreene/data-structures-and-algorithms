'use strict';

const Tree = require('../classes/binary-search-tree.js');

describe('TESTS FOR BINARY TREE AND BINARY SEARCH TREE CLASSES', () => {
  let tree = null;

  beforeEach(() => {
    tree = new Tree();
  });

  //case #1 - Create a new Binary Tree
  it('Can successfully instantiate an empty tree', () => {
    expect(tree.root).toEqual(null);
  });

  //case #2 - Add Method - Just a Root
  it('Can successfully instantiate a tree with a single root node', () => {
    tree.add(4);

    expect(tree.root.value).toEqual(4);
  });

  //case #3 - Add Method - Adding Child Objects
  it('Can successfully add a left child and right child to a single root node', () => {
    tree.add(4);
    tree.add(5);
    tree.add(2);

    expect(tree).toEqual({"root": {"left": {"left": null, "right": null, "value": 2}, "right": {"left": null, "right": null, "value": 5}, "value": 4}});
  });

  //case #4 - PreOrder Method
  it('Can successfully return a collection from a pre-order traversal', () => {
    tree.add(4);
    tree.add(6);
    tree.add(2);
    tree.add(3);
    tree.add(1);
    tree.add(5);
    tree.add(7);

    expect(tree.preOrder()).toEqual([4, 2, 1, 3, 6, 5, 7]);
  });

  //case #5 - InOrder Method
  it('Can successfully return a collection from an in-order traversal', () => {
    tree.add(4);
    tree.add(6);
    tree.add(2);
    tree.add(3);
    tree.add(1);
    tree.add(5);
    tree.add(7);

    expect(tree.inOrder()).toEqual([1, 2, 3, 4, 5, 6, 7]);
  });

  //case #6 - PostOrder Method
  it('Can successfully return a collection from an in-order traversal', () => {
    tree.add(4);
    tree.add(6);
    tree.add(2);
    tree.add(3);
    tree.add(1);
    tree.add(5);
    tree.add(7);

    expect(tree.postOrder()).toEqual([1, 3, 2, 5, 7, 6, 4]);
  });

  //case #7 - Contains Method
  it('Can successfully return true when passed a value already contained within the Binary Tree', () => {
    tree.add(4);
    tree.add(6);
    tree.add(2);
    tree.add(3);
    tree.add(1);
    tree.add(5);
    tree.add(7);

    expect(tree.contains(7)).toEqual(true);
  });
});
