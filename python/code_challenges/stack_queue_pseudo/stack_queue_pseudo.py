from stack import Stack

class PseudoQueue():
    '''
    A class simulating the functionality of a Queue, but using two stacks as the means of internal storage.
    __init__ values: None
    '''
    def __init__(self):
        self.storage_stack = Stack()
        self.overfl_stack = Stack()

    def enqueue(self, val):
        '''
        Stores a new value in the storage_stack.
        Input: self as instance, val as any value
        Output: None
        '''
        self.storage_stack.push(val)

    def dequeue(self):
        '''
        Removes a value from the storage_stack in a First-in,First-out method using a second stack to store temporary values.
        Input: None
        Output: Value of removed node
        '''
        if self.storage_stack.top == None:
            raise Exception('Empty Stack')
        else:
            curr_node = self.storage_stack.top
            while curr_node.next != None:
                self.overfl_stack.push(self.storage_stack.pop())
                curr_node = curr_node.next

            ret_val = self.storage_stack.pop()
            curr_node = self.overfl_stack.top

            while curr_node != None:
                self.storage_stack.push(self.overfl_stack.pop())
                curr_node = curr_node.next

        return ret_val

    def peek(self):
        '''
        Returns the value of the node located at the top of the storage_stack. Should raise exception when called on empty stack.
        input: None
        output: Value of top node of storage_stack
        '''
        return self.storage_stack.peek()

    def is_empty(self):
        '''
        Returns a boolean determing whether or not the storage stack is empty.
        input: None
        output: boolean
        '''
        if self.storage_stack.top == None:
            return True
        else:
            return False
