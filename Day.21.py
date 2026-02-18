# Create a contact book where users can add , view , remove , discard , store , search , update and modify contacts . 
contacts = {}
BewakufANEJA = True 
while BewakufANEJA:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Discard Contact")
    print("5. Search Contact")
    print("6. Update / Modify Contact")
    print("7. Exit")

    choice = input("Enter your choice: ")

    match choice:

        # for Adding Contact
        case "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            contacts[name] = {"phone": phone, "email": email}
            print("Contact added successfully!")

        # View Contacts
        case "2":
            if not contacts:
                print("No contacts available.")
            else:
                for name, details in contacts.items():
                    print(f"\nName: {name}")
                    print(f"Phone: {details['phone']}")
                    print(f"Email: {details['email']}")

        # Remove Contact (delete )
        case "3":
            name = input("Enter name to remove: ")
            if name in contacts:
                del contacts[name]
                print("Contact removed successfully!")
            else:
                print("Contact not found!")

        # Discarding Contact (pop)
        case "4":
            name = input("Enter name to discard: ")
            removed = contacts.pop(name, None)
            if removed:
                print("Contact discarded successfully!")
            else:
                print("Contact not found!")

        # Search Contact
        case "5":
            name = input("Enter name to search: ")
            if name in contacts:
                print("Phone:", contacts[name]["phone"])
                print("Email:", contacts[name]["email"])
            else:
                print("Contact not found!")

        #  FOT Update / Modify
        case "6":
            name = input("Enter name to update: ")
            if name in contacts:
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")

                contacts[name]["phone"] = new_phone
                contacts[name]["email"] = new_email

                print("Contact updated successfully!")
            else:
                print("Contact not found!")

        case "7":
            print("Exiting Contact Book...")
            break

        case _:
            print("Invalid choice! Try again.")
