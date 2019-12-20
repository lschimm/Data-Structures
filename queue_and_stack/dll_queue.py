import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues are first in, first out
# insert, delete/ enqueue, dequeue
# new things ADDED/ENQUEUED to tail
# REMOVES/DEQUEUES from the front
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size = self.size + 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size <= 0: # if the size/length is == 0
            return None    # return None
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size