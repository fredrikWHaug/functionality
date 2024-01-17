# linked list

# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.start = None

    # append function
    def append(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        tmp = self.start
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    # display function
    def display(self):
        current = self.start
        while current:
            print(current.data, end=' ')
            current = current.next
        print('None')

    # remove function
    def remove(self, value):
        current = self.start

        if current and current.data == value:
            self.start = current.next
            current = None
            return
        
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print('The value is not in the list')
            return
        
        prev.next = current.next
        current = None
    
# main function
def main():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(4)
    my_list.display()
    my_list.remove(2)
    my_list.display()

# main execution
if __name__ == '__main__':
    main()