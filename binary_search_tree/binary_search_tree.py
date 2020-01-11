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
            if self.left:
                self.left.insert(value)
                 # if something is on the left
                # (which there is because it starts as 'None')
                # it'll return and go through again
                # if there isn't anything, it'll insert it there
            if not self.left:
                self.left = BinarySearchTree(value) 
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        sub_tree_contains = False 
        if target < self.value:
            if not self.left:
                return False
            else: sub_tree_contains = self.left.contains(target)
        # above will be going left if the target is smaller
        # below is going right if the target is larger
        else:
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)
            return sub_tree_contains

    # Return the maximum value found in the tree
    def get_max(self):
        # larger numbers are always on the right side 
        # so we really only need to go right
        # continue to go through until we find a dead end/node with nothing on the right to it
        # the node with the dead end is the highest value
        if self.right:
            # if there is something on the right
            return self.right.get_max()
            # calls upon the function
        if not self.right:
            return self.value
            # return the value of the node
            # because that's gotta be the largest then


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left if able
        in_order_print(node.left)
        print(node.value)
        # then go right if can
        in_order_print(node.right)
        return

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
