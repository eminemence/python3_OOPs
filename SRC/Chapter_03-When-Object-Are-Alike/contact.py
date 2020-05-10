import contactlist


class Contact(object):
    all_contacts = contactlist.ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


if __name__ == "__main__":
    c1 = Contact("John A", "johna@example.net")
    c2 = Contact("John B", "johnb@example.net")
    c3 = Contact("Jenna C", "jennac@example.net")
    print([c.name for c in Contact.all_contacts.search("John")])
