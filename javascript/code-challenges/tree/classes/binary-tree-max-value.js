'use strict';

const BinarySearchTree = require('./binary-search-tree.js');

class BinaryTreeMaxValue extends BinarySearchTree {
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

module.exports = BinaryTreeMaxValue;
