from stack_and_queue.stack import Stack

class PseudoQueue():
    __init__():
        storage_stack = Stack()
        overfl_stack = Stack()

    def enqueue(self, val):
        storage_stack.push(val)

    def dequeue():
        if storage_stack.top == None:
            raise Exception('Empty Stack')
        else:
            curr_node = storage_stack.top
            while curr_node.next != None:
                overfl_stack.push(storage_stack.pop())
                curr_node = curr_node.next

            storage_stack.pop()
            curr_node = overfl_stack.top()

            while curr_node != None:
                storage_stack.push(overfl_stack.pop())
                curr_node = curr_node.next
