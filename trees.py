class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        # self.left_child = None
        # self.right_child = None

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        # self.children = [child for child in self.children if child is not node]
        new_children = []
        for child in self.children:
            if not child == node:
                new_children.append(child)
        self.children = new_children

    def traverse(self):
        nodes = [self]
        while len(nodes) != 0:
            current_node = nodes.pop()
            print(current_node.data)
            nodes += current_node.children

root = Node("Darth Vader")
child_1 = Node("Luke Skywalker")
child_2 = Node("Leia Organa")
child_3 = Node("Kylo Ren")

root.add_child(child_1)
root.add_child(child_2)
root.remove_child(child_1)
child_2.add_child(child_3)

root.traverse()