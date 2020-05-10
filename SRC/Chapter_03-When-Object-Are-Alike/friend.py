import contact


# The below class extends Contact class,
# and corrects the problem
class Friend(contact.Contact):
    def __init__(self, name, email, phone):
        # Corrected by calling super init.
        super().__init__(name, email)
        self.phone = phone
