import csv
import threading


# ------------------ CONTACT CLASS ------------------
class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, "
            f"{self.address}, {self.city}, {self.state}, "
            f"{self.zip_code}, {self.phone}, {self.email}"
        )


# ------------------ ADDRESS BOOK CLASS ------------------
class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # UC1 + UC6
    def add_contact(self, contact):
        for c in self.contacts:
            if c.first_name == contact.first_name and c.last_name == contact.last_name:
                print("❌ Duplicate contact not allowed")
                return
        self.contacts.append(contact)
        print("✅ Contact added")

    # UC2
    def edit_contact(self, first_name):
        for c in self.contacts:
            if c.first_name == first_name:
                c.city = input("New City: ")
                c.phone = input("New Phone: ")
                print("✅ Contact updated")
                return
        print("❌ Contact not found")

    # UC3
    def delete_contact(self, first_name):
        for c in self.contacts:
            if c.first_name == first_name:
                self.contacts.remove(c)
                print("✅ Contact deleted")
                return
        print("❌ Contact not found")

    # UC10
    def sort_by_name(self):
        self.contacts.sort(key=lambda c: (c.first_name, c.last_name))

    # UC11
    def sort_by_city(self):
        self.contacts.sort(key=lambda c: c.city)

    def sort_by_state(self):
        self.contacts.sort(key=lambda c: c.state)

    def sort_by_zip(self):
        self.contacts.sort(key=lambda c: c.zip_code)

    # UC12 – File IO
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for c in self.contacts:
                f.write(str(c) + "\n")
        print("✅ Data written to file")

    def read_from_file(self, filename):
        with open(filename, "r") as f:
            print(f.read())

    # UC13 – CSV
    def write_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for c in self.contacts:
                writer.writerow([
                    c.first_name, c.last_name, c.address,
                    c.city, c.state, c.zip_code, c.phone, c.email
                ])
        print("✅ CSV file written")

    def read_csv(self, filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            self.contacts.clear()
            for row in reader:
                self.contacts.append(Contact(*row))
        print("✅ CSV file read")


# ------------------ ADDRESS BOOK SYSTEM (UC5–UC9) ------------------
class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    # UC5
    def add_address_book(self, name):
        self.address_books[name] = AddressBook(name)
        print(f"✅ Address Book '{name}' created")

    # UC7
    
    def search_by_city(self, city):
        for book in self.address_books.values():
            for c in book.contacts:
                if c.city == city:
                    print(c)

    # UC8
    def view_by_city(self):
        city_map = {}
        for book in self.address_books.values():
            for c in book.contacts:
                city_map.setdefault(c.city, []).append(c)

        for city, people in city_map.items():
            print(f"\nCity: {city}")
            for p in people:
                print(p)

    # UC9
    def count_by_city(self):
        city_count = {}
        for book in self.address_books.values():
            for c in book.contacts:
                city_count[c.city] = city_count.get(c.city, 0) + 1

        for city, count in city_count.items():
            print(city, ":", count)


# ------------------ MAIN PROGRAM ------------------
def main():
    print("Welcome to Address Book Program (UC1–UC14)")

    system = AddressBookSystem()
    system.add_address_book("Default")
    book = system.address_books["Default"]

    while True:
        print("\n1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Sort by Name")
        print("6. Write to File")
        print("7. Read from File")
        print("8. Write CSV")
        print("9. Read CSV")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            contact = Contact(
                input("First Name: "),
                input("Last Name: "),
                input("Address: "),
                input("City: "),
                input("State: "),
                input("Zip: "),
                input("Phone: "),
                input("Email: ")
            )
            book.add_contact(contact)

        elif choice == "2":
            book.edit_contact(input("Enter First Name: "))

        elif choice == "3":
            book.delete_contact(input("Enter First Name: "))

        elif choice == "4":
            for c in book.contacts:
                print(c)

        elif choice == "5":
            book.sort_by_name()
            print("Sorted by Name")

        elif choice == "6":
            book.write_to_file("addressbook.txt")

        elif choice == "7":
            book.read_from_file("addressbook.txt")

        elif choice == "8":
            book.write_csv("addressbook.csv")

        elif choice == "9":
            book.read_csv("addressbook.csv")

        elif choice == "10":
            print("👋 Exiting Program")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()











