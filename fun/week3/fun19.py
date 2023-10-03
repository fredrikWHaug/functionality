
# function declaration
def email_book(email_list):
    keys_list = list(email_list.keys())
    for i in email_list:
        print(f'Employee: {keys_list[i]}\nEmail: {email_list[i]}');

# main execution
if __name__ == '__main__':
    neuralink_email_list = {0:'elon@neuralink.com', 1:'fwhaug@neuralink.com'}
    email_book(neuralink_email_list)