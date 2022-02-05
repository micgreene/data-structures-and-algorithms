from queue_node import Node

class Queue:
    def __init__(self, front = None, back = None):
        self.front = front
        self.back = back

    def __str__(self):
        return f'A Queue, its front holds {self.front}, its back holds {self.back}'

    def __repr__(self):
        return f'Queue(front: Node({self.front}), back: Node({self.back}))'

    def enqueue(self, value):
        '''
        Adds a new node with that value to the back of the queue with an O(1) Time performance.
        input: self as instance, value as any value
        output: None
        '''
        node = Node(value)

        if self.front== None:
            self.front = node
        elif self.front.next == None:
            self.back = node
            self.front.next = self.back
        else:
            self.back.next = node
            self.back = self.back.next

    def dequeue(self):
        '''
        Removes the node from the front of the queue. Should raise exception when called on empty queue.
        input: None
        output: The value of the node from the front of the queue
        '''
        if self.front == None:
            raise Exception('Queue is empty.')
        else:
            temp_front = self.front
            self.front = self.front.next

            return temp_front.value

    def peek(self):
        '''
        Returns the value of the node located at the front of the queue. Should raise exception when called on empty queue.
        input: None
        output: Value of front node of queue
        '''

        if self.front == None:
            raise Exception('Queue is empty.')
        else:
            return self.front.value

    def is_empty(self):
        '''
        Returns a boolean indicating whether or not the queue is empty
        input: None
        output: Boolean
        '''
        if self.front:
            return False
        else:
            return True
