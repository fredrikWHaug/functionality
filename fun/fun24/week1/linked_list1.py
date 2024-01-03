# linked list 

# node class initiating a node object containg some data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.start = None

    # append data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        current = self.start
        while current:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')

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
    my_list.append(1)
    my_list.append(2)
    my_list.display()
    my_list.remove(1)
    my_list.display()

# main execution
if __name__ == '__main__':
    main()