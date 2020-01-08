import sys
sys.path.append('./binary_search_tree')
from dll_queue import Queue
from dll_stack import Stack

# Start at the first node
# Nodes on the left side are always < node's key
# Nodes on the right side are always >= node's key
# the left and right subtrees must be binary search trees as well



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if the value of the node  < self.value (root node)
        # go left
        # if the value of the node  >= self.value (root node)
        # go right
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
                # if something is on the left
                # (which there is because it starts as 'None')
                # it'll return and go through again
            else:
                self.left.insert(value)
                # if there isn't anything, it'll update that value
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # larger numbers are always on the right side 
        # so we really only need to go right
        # continue to go through until we find a dead end/node with nothing on the right to it
        # the node with the dead end is the highest value
        if self.right:
            # if there is something on the right
            return self.right.get_max()
            # return that max value on the right
        if not self.right:
            return self.value
            # return the value of the node
            # because that's gotta be the largest then


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
