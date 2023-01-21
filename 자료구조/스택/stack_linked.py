class MyNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class MyStack:
    def __init__(self) -> None:
        self.head = MyNode(None)
        self.size = 0
        
    def top(self):
        if self.size == 0:
            raise IndexError()
        return self.head.next.data
    
    def pop(self):
        if self.size == 0:
            raise IndexError()
        self.size -= 1
        curr = self.head.next
        self.head.next = curr.next


    def push(self, data):
        self.size += 1
        node = MyNode(data)
        node.next = self.head.next
        self.head.next = node
        