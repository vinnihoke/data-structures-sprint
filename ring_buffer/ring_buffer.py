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
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # If storage is empty add one
        if len(self.storage) == 0:
            self.storage.append(item)
        else:
            # If len of storage == capacity
            if len(self.storage) == self.capacity:
                # Check if the index is capacity
                if self.index == self.capacity:
                    # Zero out index
                    self.index -= self.capacity
                    # Add item into storage at index
                    self.storage[self.index] = item
                    # Increment index
                    self.index += 1
                # If index is not capacity
                else:
                    # Add item into storage at index
                    self.storage[self.index] = item
                    # Increment index
                    self.index += 1
            # Len of storage is not capacity
            else:
                # Add into storage
                self.storage.append(item)
                # No need to count index's yet.

    def get(self):
        # Return the array.
        return self.storage
