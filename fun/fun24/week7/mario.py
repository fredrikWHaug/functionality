
def get_height():
    while True:
        height = int(input('Please enter an integer between 1 and 8: '))
        if 1 <= height <= 8:
            return height
    except ValueError:


def print_pyramid(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        hashes = '#' * (i + 1)
        print(spaces + hashes)
