#Contact Book
class Contact:
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

  def display_infor(self):
    print(self.name)
    print(self.phone)
    print(self.email)


class Book:
  def __init__(self):
    self.Contacts = []

  def add_contacts(self, contact):
    self.Contacts.append(contact)

  def list_contact(self):
    for contacts in self.Contacts:
      print(f"The name is: {contacts.name} \nThe PhoneNumber is: {contacts.phone} \nThe email is: {contacts.email}")


if __name__ == "__main__":
  Book = Book()

contact1 = Contact("Swat", "0197685432", "Swat@gmail.com")
contact2 = Contact("Shagor", "017878756", "Shagor@gmail.com")

Book.add_contacts(contact1)
Book.add_contacts(contact2)

print("The Boking has Done and the Contacts are:")
Book.list_contact()