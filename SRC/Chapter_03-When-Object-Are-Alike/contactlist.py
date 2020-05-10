class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name"""
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact
