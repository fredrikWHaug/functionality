
def get_height():
    while True:
        try:
            height = int(input('Please enter an integer between 1 and 8: '))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass
        print('Please enter an integer between 1 and 8')