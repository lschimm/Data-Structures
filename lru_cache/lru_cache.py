class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = dict()
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # return None if there's no key in storage
        if key not in self.storage:
            return None
        pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # stored in storage
        # create a node with the key
        if key in self.storage:
            node = self.storage[key]
            # update the value in storage
            node.value = value
            # move the current node to the tail
            self.order.move_to_end(node)
            return

        # the key doesn't exist
        # create a node with the key instead
        # add node to the tail of the list
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
        self.size >= self.limit:
            # delete the correct key
            del self.storage[self.order.head.value[0]]
            # remove the current head
            self.order.remove_from_head()
            self.size -= 1
            # remove the least recently used key: value pair
