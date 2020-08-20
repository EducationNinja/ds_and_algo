class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class Queue:
    def __init__(self, limit=10, front=None, back=None):
        self.front = front
        self.back = back
        self.limit = limit
        self.length = 0

    def peek(self):
        return self.front

    def is_full(self):
        return self.length == self.limit

    def is_empty(self):
        return self.length == 0

    def enqueue(self, data):
        if self.is_full():
            print("No more space!")
        else:
            new_node = Node(data)
            if self.is_empty():
                self.front = new_node
            else:
                self.back.set_next(new_node)
            self.back = new_node
            self.length += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            removed_node = self.front
            self.front = removed_node.get_next()
            self.length -= 1
            return removed_node.get_data()

print("You're all here to bend the knee, so get in line...")
# Creating a Queue instance
throne_room = Queue()

throne_room.enqueue("Jon Snow")
throne_room.enqueue("Arya Stark")
throne_room.enqueue("Tyrion Lannister")
throne_room.enqueue("Daenerys Targaryen")
throne_room.enqueue("Sansa Stark")
throne_room.enqueue("Ygritte")
throne_room.enqueue("Brienne of Tarth")
throne_room.enqueue("Tormund GiantsBane")
throne_room.enqueue("Oberyn Martel")
throne_room.enqueue("Margaery Tyrell")

# Queue Overflow
throne_room.enqueue("Theon Greyjoy")

print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())
print(throne_room.dequeue())

# Queue Underflow
print(throne_room.dequeue())