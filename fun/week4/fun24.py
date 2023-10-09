
# range for loop with specified increments
def skipping(cont):
    for i in range(0, 10, 5):
        print(cont[i])

# main execution
if __name__ == '__main__':
    cont = [1, 2, 3, 4, 4, 4, 6, 2, 2, 1]
    skipping(cont)