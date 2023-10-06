
# for loop basics
def item_and_length(container):
    for i in container:
        print(i, len(i));

# main execution
if __name__ == '__main__':
    example_list = ['cat', 'dog', 'mouse']
    item_and_length(example_list)