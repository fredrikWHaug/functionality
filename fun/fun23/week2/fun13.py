# multiply and add strings ... ? 
def silly_string(something):
    return something * 3 + '42069'

# main execution
if __name__ == '__main__':
    user_input = input("Hi, say a word please: ")
    print(f'''\nOk, here is what you
                said through the silly_string 
                function:\n {silly_string(user_input)}''')                
