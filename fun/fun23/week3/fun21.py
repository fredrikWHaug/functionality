
# input and control flow
def greater_than():
    x = int(input('Enter a number: '))
    if x > 0:
        print('Number is positive')
    elif x < 0:
        print('Number is negative')
    else:
        print('Number is zero')

# main execution
if __name__ == '__main__':
    greater_than()