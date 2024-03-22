
def get_height():
    while True:
        try:
            height = int(input('Enter an integer between 1 and 3: '))
            if 1 <= height <= 3:
                return height
        except ValueError:
            pass
        print('Please enter an integer between 1 and 3')

def print_pyramid(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        hashes = '#' * (i + 1)
        print(spaces + hashes)

def main():
    height = get_height()
    print_pyramid(height)

if __name__ == '__main__':
    main()