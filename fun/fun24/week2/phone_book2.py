# phone book

# add contact function
def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f'{name} successfully added')

# view contacts function
def view_contacts(contacts):
    if not contacts:
        print(f'There are no contacts')
    else:
        for name, phone in contacts.items():
            print(f'{name}: {phone}')

# delete contacts function
def delete_contacts(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f'Deleted {name} from contacts')
    else:
        print(f'{name} not found in contacts')

# main function
def main():
    contacts = {}
    add_contact(contacts, 'Fredrik', '47708418')
    view_contacts(contacts)
    delete_contacts(contacts, 'Fredrik')
    view_contacts(contacts)

# main execution
if __name__ == '__main__':
    main()