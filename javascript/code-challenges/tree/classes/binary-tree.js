'use strict';

// local module
const Node = require('./node.js');

class BinaryTree {
  constructor() {
    this.root = null;
  }

  add(val) {
    let node = new Node(val);

    if (!this.root) {
      this.root = node;

      return console.log('Node value added: ', node.value);
    }

    let currentNode = this.root;
    let trackingNode = null;

    while (currentNode !== null) {
      trackingNode = currentNode;
      if (val < currentNode.value) {
        currentNode = currentNode.left;
      } else {
        currentNode = currentNode.right;
      }
    }

    if (val < trackingNode.value) {
      trackingNode.left = node;
    } else {
      trackingNode.right = node;
    }

    return console.log('Node value added: ', node.value);
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

  contains(value) {
    let currentNode = null;
    let containsNum = null;
    let _walk = (node) => {
      currentNode = node;

      if (currentNode === null) {
        containsNum = false;
        return false;
      }

      if (currentNode.value === value) {
        containsNum = true;
        return true;
      }

      let leftNodes = _walk(node.left);

      if (leftNodes === true) {
        containsNum = true;
        return true;
      }

      let rightNodes = _walk(node.right);

      if (rightNodes === true) {
        containsNum = true;
        return true;
      }
    };
    _walk(this.root);

    return containsNum;
  }

  findMaximumValue() {
    let max = this.root.value;

    let nodeChecker = (node) => {

      if (node.value > max) {
        max = node.value;
      }
      if (node.left) {
        nodeChecker(node.left);
      }
      if (node.right) {
        nodeChecker(node.right);
      }
    };
    nodeChecker(this.root);

    return max;
  }
}

module.exports = BinaryTree;
