'use strict';

class BinaryTree {
  constructor() {
    this.root = null;
  }

  preOrder() {
    if (!this.root) {
      return 'Empty Tree!';
    }

    let nodes = [];

    let _walk = (node) => {
      nodes.push(node.value);
      if (node.left) { _walk(node.left); }
      if (node.right) { _walk(node.right); }
    };

    _walk(this.root);

    return nodes;
  }

  inOrder() {
    if (!this.root) {
      return 'Empty Tree!';
    }

    let nodes = [];

    let _walk = (node) => {
      if (node.left) { _walk(node.left); }
      nodes.push(node.value);
      if (node.right) { _walk(node.right); }
    };

    _walk(this.root);

    return nodes;
  }

  postOrder() {
    if (!this.root) {
      return 'Empty Tree!';
    }

    let nodes = [];

    let _walk = (node) => {
      if (node.left) { _walk(node.left); }
      if (node.right) { _walk(node.right); }
      nodes.push(node.value);
    };

    _walk(this.root);

    return nodes;
  }

  breadthFirst() {
    if (!this.root) {
      return 'Empty Tree!';
    }

    let iteration = 0;
    let nodes = [];
    let queue = [];

    queue.push(this.root);

    while (queue.length > 0) {
      let currentNode = queue.shift();
      nodes.push(currentNode.value);

      if (currentNode.left) {
        queue.push(currentNode.left);
      }
      if (currentNode.right) {
        queue.push(currentNode.right);
      }

      
    }
    return nodes;
  }
}

module.exports = BinaryTree;
