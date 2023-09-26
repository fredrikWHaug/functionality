# string to number
def length_of_stringy_number(number):
    collection = []
    for i in number:
        collection.append(i)
    return len(collection)

# main execution
if __name__ == '__main__':
    print(length_of_stringy_number('529'))
