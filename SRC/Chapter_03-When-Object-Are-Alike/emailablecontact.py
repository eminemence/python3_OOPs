import contact
import mailsender


class EmailableContact(contact.Contact, mailsender.MailSender):
    pass
