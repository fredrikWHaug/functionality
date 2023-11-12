
# staircase function
def staircase(steps):
    step = '#'
    for i in range(steps):
        print(step)
        step = step + '#'

# main execution
if __name__ == '__main__':
    staircase(5)