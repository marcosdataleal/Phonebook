class Contact:
  def __init__(self, name, phone):
      self.name = name
      self.phone = phone

class PhoneBook:
  def __init__(self):
      self.contacts = []

  def add_contact(self, name, phone):
      new_contact = Contact(name, phone)
      self.contacts.append(new_contact)
      print(f'Contact {name} added successfully.')

  def display_contacts(self):
      if not self.contacts:
          print('The phone book is empty.')
      else:
          print('List of Contacts:')
          for contact in self.contacts:
              print(f'{contact.name}: {contact.phone}')

  def search_contact(self, name):
      for contact in self.contacts:
          if contact.name.lower() == name.lower():
              print(f'Contact found: {contact.name} - {contact.phone}')
              return
      print(f'Contact "{name}" not found in the phone book.')

if __name__ == "__main__":
  phone_book = PhoneBook()

  while True:
      print("\nChoose an option:")
      print("1 - Add Contact")
      print("2 - Display Contacts")
      print("3 - Search Contact")
      print("0 - Exit")

      option = input("Enter the number of the desired option: ")

      if option == "1":
          name = input("Enter the name of the contact: ")
          phone = input("Enter the phone number of the contact: ")
          phone_book.add_contact(name, phone)
      elif option == "2":
          phone_book.display_contacts()
      elif option == "3":
          name = input("Enter the name of the contact you want to search for: ")
          phone_book.search_contact(name)
      elif option == "0":
          print("Closing the phone book. Goodbye!")
          break
      else:
          print("Invalid option. Please try again.")

