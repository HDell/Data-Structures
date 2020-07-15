"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes. DLL.delete()
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value): #OK
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            new_node = ListNode(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self): #OK
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return value
        
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value): #OK
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self): #OK
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else: 
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node): #OK
        if self.length > 1:
            if node is not self.tail and node is not self.head:
                node.prev.next, node.next.prev = node.next, node.prev
            elif node is self.head:
                return
            else: #node is self.tail
                node.prev.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node 
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node): #OK
        if self.length > 1:
            if node is not self.head and node is not self.tail:
                node.prev.next, node.next.prev = node.next, node.prev
            elif node is self.tail:
                return
            else: #node is self.head
                node.next.prev = None
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node): #OK
        if self.length == 1: # Only Node
            self.head = None
            self.tail = None
        elif node is self.head:
            node.next.prev = node.prev
            self.head = node.next
            node.next = None 
        elif node is self.tail:
            node.prev.next = node.next
            self.tail = node.prev
            node.prev = None
        else:
            node.prev, node.next = node.next, node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self): #OK
        if self.length > 0:
            current_node = self.head
            current_max = self.head.value
            while current_node is not self.tail:
                current_node = current_node.next
                if current_node.value > current_max:
                    current_max = current_node.value
            return current_max