import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

# Search contact by name or phone
def search_contact(contacts):
    key = input("Enter name or phone number to search: ").lower()
    results = [c for c in contacts if key in c["name"].lower() or key in c["phone"]]
    if results:
        for contact in results:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("❌ No contact found.")

# Update contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep current value.")
            new_name = input(f"New name [{contact['name']}]: ") or contact["name"]
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
            new_email = input(f"New email [{contact['email']}]: ") or contact["email"]
            new_address = input(f"New address [{contact['address']}]: ") or contact["address"]

            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            save_contacts(contacts)
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name:
            del contacts[i]
            save_contacts(contacts)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

# Main menu
def menu():
    contacts = load_contacts()
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    menu()
