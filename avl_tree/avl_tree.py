"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        self.height = -1

        if self.node:
            self.height = 0

            if self.node.left:
                self.node.left.update_height()
                self.height = 1 + self.node.left.height
            
            if self.node.right:
                self.node.right.update_height()
                height = 1 + self.node.right.height
                if height > self.height:
                    self.height = height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        self.balance = 0
        
        if self.node:
            if self.node.left and self.node.right:
                self.balance = self.node.left.height - self.node.right.height
            elif self.node.left:
                self.balance = 1
            elif self.node.right:
                self.balance = -1

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        node = self.node

        if not node:
            self.node = Node(key)
            return

        if key >= node.key:
            if node.right:
                node.right.insert(key)
            else:
                node.right = AVLTree(Node(key))
        if key < node.key:
            if node.left:
                node.left.insert(key)
            else:
                node.left = AVLTree(Node(key))
