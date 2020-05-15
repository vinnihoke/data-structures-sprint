class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# Queue with limited size that repeats when full - FIFO


class RingBuffer:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def get(self):


buffer = RingBuffer(3)

buffer.append("a")
buffer.append("b")
buffer.append("b")
# print(buffer.head.get_value())
# buffer.append("b")
# print(buffer.head.get_value())
# buffer.append("c")
# print(buffer.head.get_value())
# buffer.append("d")
# print(buffer.head.get_value())
# buffer.append("d")
# print(buffer.head.get_value())
# buffer.get()
