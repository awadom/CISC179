def read_address_book(file_path):
    address_book = {}
    with open(file_path) as file:
        lines = file.read().splitlines()
        for i in range(0, len(lines), 2):
            name = lines[i]
            email = lines[i + 1]
            address_book[name] = email
    return address_book


def write_address_book(file_path, address_book):
    with open(file_path, "w") as file:
        for name, email in sorted(address_book.items()):
            file.write(name + "\n")
            file.write(email + "\n")


def lookup_email(address_book):
    name = input("Enter name:")
    if name in address_book:
        print(address_book[name])
    else:
        print("Sorry, no contact exists under that name.")


def add_contact(address_book):
    name = input("Enter name:")
    email = input("Enter email address:")
    address_book[name] = email


def change_email(address_book):
    name = input("Enter name:")
    if name in address_book:
        new_email = input("Enter new email address:")
        address_book[name] = new_email
    else:
        print("Sorry, no contact exists under that name.")


def delete_contact(address_book):
    name = input("Enter name:")
    if name in address_book:
        del address_book[name]
    else:
        print("Sorry, no contact exists under that name.")


# Main program
file_path = "./Module 6/phonebook.in"
address_book = read_address_book(file_path)

while True:
    print("Enter")
    print("1) look up an email address")
    print("2) add a new name and email address")
    print("3) change an email address")
    print("4) delete a name and email address")
    print("5) save address book and exit:", end="")
    choice = input()
    if choice == "1":
        lookup_email(address_book)
    elif choice == "2":
        add_contact(address_book)
    elif choice == "3":
        change_email(address_book)
    elif choice == "4":
        delete_contact(address_book)
    elif choice == "5":
        write_address_book("./Module 6/phonebook.out", address_book)
        print()
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
