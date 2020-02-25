import os
import sys

queue_stack_path = os.path.normpath(os.path.join(__file__, '../../queue_and_stack'))
sys.path.append(queue_stack_path)

from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        if value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value and self.right != None:
            return self.right.contains(target)
        if target < self.value and self.left != None:
            return self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, *args):
        if self.left != None:
            self.left.in_order_print()
        print(self.value)
        if self.right != None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, *args):
        q = Queue()
        q.enqueue(self)
        while q.len():
            node = q.dequeue()
            print(node.value)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, *args):
        s = Stack()
        s.push(self)
        while s.len():
            node = s.pop()
            print(node.value)
            if node.left != None:
                s.push(node.left)
            if node.right != None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, *args):
        print(self.value)
        if self.left != None:
            self.left.pre_order_dft()
        if self.right != None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, *args):
        if self.left != None:
            self.left.post_order_dft()
        if self.right != None:
            self.right.post_order_dft()
        print(self.value)
