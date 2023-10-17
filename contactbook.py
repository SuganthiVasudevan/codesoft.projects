contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
    print(f"{name} has been added to your contacts.")

def view_contact_list():
    print("Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone Number: {info['phone_number']}")

def search_contact(query):
    results = []
    for name, info in contacts.items():
        if query in name or query in info['phone_number']:
            results.append((name, info))
    return results

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating {name}'s information:")
        phone_number = input(f"New phone number for {name}: ")
        email = input(f"New email for {name}: ")
        address = input(f"New address for {name}: ")
        contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print(f"{name}'s contact information has been updated.")
    else:
        print(f"{name} not found in contacts.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact has been deleted successfully.")
    else:
        print(f"{name} not found in contacts.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        results = search_contact(query)
        if results:
            for name, info in results:
                print(f"Name: {name}, Phone Number: {info['phone_number']}")
        else:
            print("No matching contacts found.")
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Management System.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
