from django.test import TestCase
from user_contacts.models import Person
from user_contacts.new_contact_form import ContactForm

class TestContactForm(TestCase):
    def test_if_valid_contact_is_saved(self):
        form = ContactForm({'first_name':'test', 'last_name':'test','number':'9999900000'})
        contact = form.save()
        self.assertEqual(contact.person.first_name, 'test')
    def test_if_invalid_contact_is_not_saved(self):
        form = ContactForm({'first_name':'tes&t', 'last_name':'test','number':'9999900000'})
        contact = form.save()
        self.assertEqual(contact, None)
