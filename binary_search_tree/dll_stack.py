import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

## Stack is Last in, first out
#    ___
#   _____
#  ________
# it brings/PUSHES items up and items come/POP off  the top
# add to the tail, remove from the head

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size = self.size + 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size <= 0: # if the size is less than or equal to 0
            return None # return None because nothing to return
        if self.size > 0:  # if the size is greater than 0
            self.size = self.size - 1 # We gotta return that something
            return self.storage.remove_from_head() # from the head (pop off the top)
        else:
            return None

    def len(self):
        return self.size