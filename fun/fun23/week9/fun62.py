# mario script

# get height
def get_height():
    while True:
        try:
            height = int(input('Enter an integer between 1 and 8: '))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass
        print('Please enter a value between 1 and 8')

# print pyramid function
def print_pyramid(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        hashes = '#' * (i + 1)
        print(spaces + hashes)

# main function
def main():
    height = get_height()
    print_pyramid(height)

# main execution
if __name__ == '__main__':
    main()