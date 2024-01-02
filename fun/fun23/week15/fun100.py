# linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def append(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        last_node = self.start
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.start
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()    