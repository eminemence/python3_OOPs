import contact


# The below class extends Contact class,
# but there is duplicate code, which we correct in next version.
class Friend(contact.Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
