# linked list

# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list class
class LinkedList:
    def __init__(self):
        self.start = None

    def append(self, data):
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
            return
        tmp = self.start
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
    