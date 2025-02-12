from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
        else: 
            node = self.head
            while node.nxt is not None:
                node = node.nxt
            node.nxt = new
        self.size += 1


    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{"
        node = self.head
        while node is not None:
            s += str(node.val) + " "
            node = node.next
        s += "}"
        return s 

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.tail is None:
            self.tail = new
        else:
            node = self.tail
            while node.nxt is not None:
                node = node.nxt
            node.nxt = new 
        self.size += 1
    

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self, n):
        if self.tail is None:
            print("its an empty deque")
            return None
        else:
            return self.tail.value
        

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self, l):
        if self.head is None:
            print("get cant be applied an empty list")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self, n):
        if self.head is None:
            print("remove cant be applied on an empty list")
        elif n < 0 or n >= self.size:
            print(f" Access outside lsit index range [0, {self.size}]")
        elif n == 0:
            self.head = self.head.nxt
            self.size -= 1
        else:
            before = self.head
            for i in range (n-1):
                before = before.nxt
            delete = before.nxt
            before.nxt = delete.nxt
            self.size -= 1



    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        pass
