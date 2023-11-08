
def mario(height):
    block = ""
    for i in range(height):
        block += "#"
    for i in range(height):
        print(block)
        block = block - "#"

if __name__ == '__main__':
    mario(8)