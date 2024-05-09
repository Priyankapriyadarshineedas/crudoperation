from datetime import date
from .models import Person, Address
from django.test import TestCase
from django.urls import reverse


class PersonModelTest(TestCase):
    def setUp(self):
        Person.objects.create(name='lkjhg', dob=date(2000, 1, 1), gen='M', reg='123456', password='admin')

    def test_person_creation(self):
        lkjhg = Person.objects.get(name='lkjhg')
        self.assertEqual(lkjhg.name, 'lkjhg')
        self.assertEqual(lkjhg.dob, date(2000, 1, 1))
        self.assertEqual(lkjhg.gen, 'M')
        self.assertEqual(lkjhg.reg, '123456')
        self.assertEqual(lkjhg.password, 'admin')

    def test_get_full_Person(self):
        person = Person.objects.get(name='lkjhg')
        self.assertEqual(person.get_full_Person(), 'lkjhg, 123456')


class AddressModelTest(TestCase):
    def setUp(self):
        person1 = Person.objects.create(name='aaa', dob='2000-01-01', gen='M', reg='123456', password='admin')
        person2 = Person.objects.create(name='bbb', dob='2000-06-01', gen='F', reg='789012', password='admin')

        address = Address.objects.create(
            street='mnop',
            city='ghyuu',
            state='hgf',
            zipcode='12345'
        )
        address.persons.add(person1, person2)
        address.save()

    def test_get_full_address(self):
        address = Address.objects.get(street='mnop')
        self.assertEqual(address.get_full_address(), 'mnop, ghyuu')


class PersonAPITests(TestCase):
    def test_create_person(self):
        data = {
            'name': 'wertrt',
            'dob': '2000-01-01',
            'gen': 'M',
            'reg': 34534534,
            'password': 'admin'
        }

        response = self.client.post(reverse('index'), data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(Person.objects.count(), 1)

        person = Person.objects.first()
        self.assertEqual(person.name, 'wertrt')

        self.assertEqual(person.reg, '34534534')


class AddressAPITests(TestCase):
    def test_create_address(self):
        data = {
            'street': 'kkldfkj',
            'city': 'jdfffd',
            'state': 'dfgfg',
            'zipcode': 354554,
            'person_id': 1,
            'person_id': 2
        }
        response = self.client.post(reverse('address'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Address.objects.count(), 1)
        address = Address.objects.first()
        self.assertEqual(address.street, 'kkldfkj')

        self.assertEqual(address.state, 'dfgfg')
