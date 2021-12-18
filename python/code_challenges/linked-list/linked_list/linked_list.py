class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return f'The Node with a value of {self.value}'

    def __repr__(self):
        return f'Node(value: {self.value}, next: {self.next})'

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return f'The Linked List with a head value of {self.head.value}'

    def __repr__(self):
        return f'Linked_List(head: {self.head})'

    def append(self, val):
        '''
        Appends a new node to the end of the linked list
        Input: self as instance, val as any value
        Output: None
        '''
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next

            curr_node.next = node

    def insert(self, val):
        '''
        Inserts a new node as the new head of the linked list
        Input: self as instance, val as any value
        Output: None
        '''
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            temp_head = self.head
            self.head = node
            self.head.next = temp_head

    def includes(self, val):
        curr_node = self.head

        while curr_node:
            if curr_node.value == val:
                return True
            else:
                curr_node = curr_node.next

        return False

    def to_string(self):
        '''
        Outputs a stringified version of the linked list
        Input: self as instance
        Output: ret_string as string
        '''
        ret_string =''

        if self.head == None:
            ret_string = '{None}'
        else:
            ret_string += '{}{}{}'.format('{ ',self.head.value,' }')
            curr_node = self.head

            while curr_node.next:
                ret_string += ' -> {}{}{}'.format('{ ',curr_node.next.value,' }')
                curr_node = curr_node.next

            ret_string += f' -> NONE'

        return ret_string
