
def print_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        hashes = '#' * (i + 1)
        print(spaces + hashes)

def main():
    height = int(input('Height: '))
    print_triangle(height)

if __name__ == '__main__':
    main()