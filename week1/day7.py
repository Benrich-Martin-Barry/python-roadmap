def add_contact(contacts, name, phone):
    contacts[name] = phone

def show_all(contacts):
    if not contacts:
        print("No contacts yet.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
def search_contact(contacts, name):
    return contacts.get(name)

def delete_contact(contacts, name):
  if name in contacts:
    del contacts[name]
    return True
  else:
    return False
contacts = {}

while True:
    print("\n1. Add  2. Search  3. Delete  4. Show all  5. Quit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name:")
        phone = input("Phone: ")
        add_contact(contacts, name, phone)
    elif choice == "2":
      name = input("Name:")
      result = search_contact(contacts, name)
      if result is None:
        print("Not found")
      else:
        print(f"{name}: {result}")
        
    elif choice == "3":
        name = input("Name:")
        if delete_contact(contacts, name):
           print("Deleted")
        else:
           print("Not found")
        
    elif choice == "4":
        show_all(contacts)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

                        