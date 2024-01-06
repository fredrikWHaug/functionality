# dictionary work

# add contacts
def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f'Contact {name} successfully added')

# view contacts
def view_contacts(contacts):
    if not contacts:
        print('No contacts found')
    else:
        print('Contacts: ')
        for name, phone in contacts.items():
            print(f'{name}: {phone}')

# delete contacts
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f'{name} deletet successfully')
    else:
        print(f'{name} not found')

# main function
def main():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            add_contact(contacts, name, phone)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(contacts, name)

        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()