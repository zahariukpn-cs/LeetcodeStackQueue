class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = new_node

    def pop(self):
        if self.head is None:
            return
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data

class MyStack:

    def __init__(self):
        self.active_q = Queue()
        self.cloud_q = Queue()

    def push(self, x: int) -> None:
        while not self.active_q.is_empty():
            self.cloud_q.push(self.active_q.pop())
        self.active_q.push(x)
        while not self.cloud_q.is_empty():
            self.active_q.push(self.cloud_q.pop())
        self.cloud_q = Queue()

    def pop(self) -> int:
        val = self.active_q.pop()
        return val

    def top(self) -> int:
        return self.active_q.peek()

    def empty(self) -> bool:
        return self.active_q.is_empty() and self.cloud_q.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
