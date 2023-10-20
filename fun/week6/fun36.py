
# optional arguments function
def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ['yes', 'y']:
            return True
        if ok in ['no', 'n']:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# main execution
if __name__ == '__main__':
    ask_ok('Can hard drive be overwritten? ', 1, 'try again please my friend')