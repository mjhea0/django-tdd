from django.template.loader import render_to_string
from django.test import TestCase, Client
from UserContacts.models import Person, Phone
from UserContacts.views import *

class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()
        self.person = Person(first_name = 'TestFirst',last_name = 'TestLast')
        self.person.save()
        self.phone = Phone(person = self.person,number = '7778889999')
        self.phone.save()

    def test_view_home_route(self):
        response = self.client_stub.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_contacts_route(self):
        response = self.client_stub.get('/all/')
        self.assertEquals(response.status_code, 200)

    def test_add_contact_route(self):
        response = self.client_stub.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_create_contact_successful_route(self):
        response = self.client_stub.post('/create',data = {'first_name' : 'testFirst', 'last_name':'tester', 'email':'test@tester.com', 'address':'1234 nowhere', 'city':'far away', 'state':'CO', 'country':'USA', 'number':'987654321'})
        self.assertEqual(response.status_code, 302)

    def test_create_contact_unsuccessful_route(self):
        response = self.client_stub.post('/create',data = {'first_name' : 'tester_first_n@me', 'last_name':'test', 'email':'tester@test.com', 'address':'5678 everywhere', 'city':'far from here', 'state':'CA', 'country':'USA', 'number':'987654321'})
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.phone.delete()
        self.person.delete()



