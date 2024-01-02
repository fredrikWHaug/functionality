
# right aligned stair case function
def stair_case(n):
    stair_case = '#'
    for i in range(n):
        print(stair_case)
        stair_case += '#'

# main execution
if __name__ == '__main__':
    stair_case(5)