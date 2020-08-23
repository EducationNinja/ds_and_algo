class Node:
    def __init__(self, group_size, next=None):
        self.group_size = group_size
        self.next = next

    def get_group_size(self):
        return self.group_size

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
        self.waiting_time = 0

    def peek(self):
        return self.waiting_time

    def is_full(self):
        return self.length == self.limit

    def is_empty(self):
        return self.length == 0

    def add_node(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next(new_node)
        self.back = new_node
        self.length += 1
        self.waiting_time += (data*0.5)

    def enqueue(self, data):
        if self.is_full():
            print("No more space!")
        else:
            groups, remainder = divmod(data, 12)
            for i in range(groups):
                self.add_node(12)
            if remainder:
                self.add_node(remainder)

    def enqueue(self, data):
        if self.is_full():
            print("No more space!")
        else:
            people_num = data
            while people_num > 12:
                self.add_node(12)
                people_num -= 12
            self.add_node(people_num)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            removed_node = self.front
            self.front = removed_node.get_next()
            self.length -= 1
            self.waiting_time -= (removed_node.get_group_size() * 0.5)
            return removed_node.get_group_size()

hamzas_vc = Queue(10)
print(hamzas_vc.waiting_time)
print("-"*50)
hamzas_vc.enqueue(5)
hamzas_vc.enqueue(15)
hamzas_vc.enqueue(25)
hamzas_vc.enqueue(1)
print(hamzas_vc.length) # 7
print("-"*50)
print(hamzas_vc.waiting_time) # 23
print("-"*50)
hamzas_vc.dequeue()
print(hamzas_vc.length) # 6
print("-"*50)
print(hamzas_vc.waiting_time) # 20.5
print("-"*50)