# left aligned pyramid
def lef_aligned_pyramid(n):
    hashes = '#'
    for i in range(n):
        print(hashes)
        hashes = hashes + '#'

# main function
def main():
    lef_aligned_pyramid(5)

# main execution
if __name__ == '__main__':
    main()