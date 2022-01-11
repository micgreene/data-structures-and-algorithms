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

    def insert_before(self, new_Val, search_Val):
        '''
        Inserts a new node at the position prior to that of the search value in the linked list.
        Input: self as instance, new_Val as any value, search_Val as a value already in the linked list
        Output: None
        '''
        curr_Node = self.head
        prev_Node = Node(None)
        input_node = Node(new_Val)

        try:
            if self.head == None:
                self.head = input_node
            else:
                while curr_Node.next:
                    if curr_Node.value == search_Val:
                        if prev_Node.value == None:
                            self.head = input_node
                            self.head.next = curr_Node
                            return
                        else:
                            prev_Node.next = input_node
                            input_node.next = curr_Node
                            return

                    prev_Node = curr_Node
                    curr_Node = curr_Node.next
                raise ValueError

        except ValueError:
                    print('The search value cannot be found in this linked list!')

    def insert_after(self, new_Val, search_Val):
        '''
        Inserts a new node at the position after that of the search value in the linked list.
        Input: self as instance, new_Val as any value, search_Val as a value already in the linked list
        Output: None
        '''
        curr_Node = self.head
        input_node = Node(new_Val)
        try:
            if self.head == None:
                self.head = input_node
            elif curr_Node.next == None:
                curr_Node.next = input_node
            else:
                while curr_Node.next:
                    if curr_Node.value == search_Val:
                        input_node.next = curr_Node.next
                        curr_Node.next = input_node
                    curr_Node = curr_Node.next
                if curr_Node.value == search_Val:
                    curr_Node.next = input_node
                else:
                    raise ValueError

        except ValueError:
                    print('The search value cannot be found in this linked list!')


    def includes(self, val):
        '''
        Determines whether or not the linked list contains a certain value
        Input: self as instance, val as any value
        Output: Bool
        '''
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

    def kthfromend(self, k):
        '''
        Returns the value of the node the kth position from the end of the list
        Input: self as instance, k as a number
        Output: Any value of a Node
        '''

        curr_node = self.head

        node_count = 0

        if self.head == None:
            return None
        else:
            while(curr_node != None):
                node_count = node_count + 1
                curr_node = curr_node.next

        curr_node = self.head

        node_count = node_count - k
        temp_count = 0

        if node_count <= 0:
            raise ValueError('Selected number out of list index!')

        else:
            while curr_node:
                temp_count = temp_count + 1

                if temp_count == node_count:
                    return curr_node.value
                else:
                    curr_node = curr_node.next




