
def slice_tutorial():
    my_list = []
    my_list = input('Enter a number of things without whitespace in between elements. ')
    for i in my_list:
        i = int(i);
    print(type(my_list[0]));

if __name__ == '__main__':
    slice_tutorial()