"""A nice module."""
class Node:
    """A nice class."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    """A nice class."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, next=self.head)

    def pop(self):
        if self.head is None:
            return
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        return self.head.data

class MyQueue:
    """A nice class."""

    def __init__(self):
        self.inside_stck = Stack()
        self.outside_stck = Stack()

    def push(self, x: int) -> None:
        # if self.inside_stck.is_empty():
        #     self.inside_stck.head = Node(x)
        #     return
        self.inside_stck.push(x)

    def transfer_stocks(self):
        """Moves elements from income stock to outcome stock
        thus changing the order from LIFO to FIFO."""
        if not self.outside_stck.is_empty():
            return
        while not self.inside_stck.is_empty():
            self.outside_stck.push(self.inside_stck.pop())

    def pop(self) -> int:
        if self.outside_stck.is_empty() and self.inside_stck.is_empty():
            return

        self.transfer_stocks()

        val = self.outside_stck.pop()
        return val

    def peek(self) -> int:
        self.transfer_stocks()
        return self.outside_stck.peek()

    def empty(self) -> bool:
        return self.outside_stck.is_empty() and self.inside_stck.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(4)
# param_2 = obj.pop()
# print(param_2)

# param_3 = obj.peek()
# print(param_3)

# param_4 = obj.empty()
# print(param_4)
