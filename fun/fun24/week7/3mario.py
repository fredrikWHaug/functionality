# mario

# get height function
def get_height():
    while True:
        try:
            height = int(input('Enter an integer between 1 and 8: '))
            if 1 <= height <= 1:
                return height
        except ValueError:
            pass
        print('Please enter an integer between 1 and 8')

# print pyramid
def print_pyramid(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        hashes = '#' * (i + 1)
        print(spaces + hashes)

