# Linked List
# a class of head and tail references
# no access to middle of the list
# tail gives fast access to the end of the list
# tail cannot refer back to the penultimate element in the linked list


# head            tail
# 12 ----> 39 ----> 5 ----> N (none)
#         value

# to ADD something to the linkedlist
# you can use insert i.e. list.insert(15)
# this will wrap it in a new node, 

# cons of linked list...
# linked lists do not store elements contiguously
# linked lists are not cache friendly since caches are typically optimized for contigous memory accesses

# pros!
# it's easier to insert into and delete from the middle of a list
# we can keep adding elements to linked lists ars much as needed
# (arrays have a static amount of allocated memory)

class Node:
    self.value = ValueError
    self.next = next_node

class LinkedList:
    self.head = head_node
    self.tail = tail_node