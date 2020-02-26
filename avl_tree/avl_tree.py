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
        parent = self.node
        child = self.node.right.node
        self.node = child
        parent.right = child.left
        child.left = AVLTree(parent)

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        parent = self.node
        child = self.node.left.node
        self.node = child
        parent.left = child.right
        child.right = AVLTree(parent)

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        self.update_height()
        self.update_balance()

        if self.balance < 0:
            self.node.right.rebalance()
            self.left_rotate()

        elif self.balance > 0:
            self.node.left.rebalance()
            self.right_rotate()
        
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

        while True:
            if key >= node.key:
                if node.right:
                    node = node.right.node
                else:
                    node.right = AVLTree(Node(key))
                    break
            if key < node.key:
                if node.left:
                    node = node.left.node
                else:
                    node.left = AVLTree(Node(key))
                    break

        self.update_height()
        self.update_balance()
        if self.balance < -1 or self.balance > 1:
            self.rebalance()

tree = AVLTree()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(7)
tree.display()
tree.insert(8)
tree.display()