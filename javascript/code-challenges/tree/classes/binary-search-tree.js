'use strict';

const { root } = require('cheerio');
const BinaryTree = require('./binary-tree.js');
const Node = require('./node.js');

class BinarySearchTree extends BinaryTree {
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
}

module.exports = BinarySearchTree;
