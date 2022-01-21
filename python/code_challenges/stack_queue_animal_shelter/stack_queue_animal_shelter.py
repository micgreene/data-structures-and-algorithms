from stack import Stack
from animal import Animal

class AnimalShelter ():
    '''
    A class simulating the functionality of an animal shelter, storing 'animal' objects in a First In, First Out format. Animal objects should only be a 'cat' or a 'dog'.
    Attributes:
        self.storage_stack: main storage data structure of animal objects
        self.overfl_stack: used to sort between cat and dog objects when dequeuing.
    '''
    def __init__(self):
        self.storage_stack = Stack()
        self.overfl_stack = Stack()

    def __str__(self):
        return f'The Animal Shelter, its longest resident is {self.storage_stack.top}'

    def __repr__(self):
        return f'AnimalShelter(self.storage_stack.top:{self.storage_stack.top})'

    def enqueue(self, name, species):
        '''
        Stores a new animal in the storage_stack.
        Input: self as instance, name as a string, species as a string
        Output: None
        '''
        new_animal = Animal(name, species)
        self.storage_stack.push(new_animal)

    def dequeue(self, pref=None):
        '''
        Removes an animal from the storage_stack in a First-in,First-out method. Uses a second stack to store and compare animals species to the preference of the user, then reassembles the shelter storage based on the results.
        Input: Pref: optional as string, default is None (should only be 'cat' or 'dog')
        Output: Value of removed animal object
        '''
        if pref:
            pref = pref.lower()

        if pref != 'cat' and pref != 'dog' and pref != None:
            raise Exception('Preference must be a Dog, a Cat, or Nothing!')

        if self.storage_stack.top == None:
            raise Exception('Empty Shelter')
        else:
            curr_node = self.storage_stack.top
            while curr_node != None:
                self.overfl_stack.push(self.storage_stack.pop())
                curr_node = curr_node.next

            ret_val = None
            curr_node = self.overfl_stack.top

            while curr_node != None:
                if pref == None and ret_val == None:
                    curr_node = curr_node.next
                    ret_val = self.overfl_stack.pop()
                    continue
                elif ret_val == None:
                    if pref == 'dog' and curr_node.value.species == 'dog':
                        ret_val = curr_node.value
                        curr_node = curr_node.next
                        self.overfl_stack.pop()
                        continue
                    elif pref == 'cat' and curr_node.value.species == 'cat':
                        ret_val = curr_node.value
                        curr_node = curr_node.next
                        self.overfl_stack.pop()
                        continue

                self.storage_stack.push(self.overfl_stack.pop())
                curr_node = curr_node.next

        return ret_val
