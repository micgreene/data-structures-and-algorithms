from binary_search_tree import BinarySearch
from queue import Queue

def breadth_first(tree):
    ret_list = []
    node_queue = Queue()

    node_queue.enqueue(tree.root)
    while node_queue.is_empty() == False:
        temp_node = node_queue.dequeue()
        ret_list.append(temp_node.value)

        if temp_node.left:
            node_queue.enqueue(temp_node.left.value)
        if temp_node.right:
            node_queue.enqueue(temp_node.right.value)

    return ret_list
