import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues are first in, first out
# insert, delete/ enqueue, dequeue
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size = self.size + 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size == 0:
            return None
        # if self.size > 0:
        #     return self.size -= 1 # not needed since code below takes care of this
        else:
            self.size = self.size - 1
            return self.storage.remove_from_tail()

    def len(self):
        pass
    