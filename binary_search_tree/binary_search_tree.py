"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value >= self.value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value: #search right subtree
            if self.right is not None:
                return self.right.contains(target)
            else: 
                return False
        else: #target < self.value #search left subtree
            if self.left is not None:
                return self.left.contains(target)
            else: 
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        if self.right is not None:
            return self.right.get_max()
        else:
            return current_max
                    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.value is None:
            return

        if self.left is not None:
            self.left.in_order_print(self.left) 

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self) 
        while queue.size > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size > 0:
            current = stack.pop()
            print(current.value)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if self.value is None:
            return

        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft(self.left) 

        if self.right is not None:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.value is None:
            return

        if self.left is not None:
            self.left.post_order_dft(self.left) 

        if self.right is not None:
            self.right.post_order_dft(self.right)

        print(self.value)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            value = self.storage[0]
            self.storage = self.storage[1:]
            self.size -= 1
            return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            value = self.storage[self.size - 1]
            self.storage = self.storage[0:self.size - 1]
            self.size -= 1
            return value
        return None
        