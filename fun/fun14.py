
second_to_last_character = ''
def slicing_fun(word):
    second_to_last_character = word[-2];
    second_to_last_character += ' hi'
    second_to_last_character += 'u'*2
    return second_to_last_character

if __name__ == '__main__':
    my_word = 'himom'
    print(slicing_fun(my_word))
    print("I'm not going to lie")
    print('''To me, it's strange that we 
can multiply characters together
and add and subtract them''')
