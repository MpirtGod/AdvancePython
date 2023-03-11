import unittest
from mod3.task4 import Person

class TestInit(unittest.TestCase):
    def test_valid_values(self):
        person = Person(name='Саша', year_of_birth=2002)
        person.name = 'Серега'
        person.yob = 2010
        person.address = 'Have'
        person2 = person
        self.assertTrue(person2.name == 'Серега' and person2.yob == 2010 and person2.address == 'Have')

    def test_get_age(self):
        person = Person(name='Саша', year_of_birth=2002)
        self.assertEqual(person.get_age(), 21)

    def test_get_age_throw_error(self):
        person = Person(name='Саша', year_of_birth='2022')
        self.assertRaises(TypeError)

    def test_get_name(self):
        person = Person(name='Саша', year_of_birth=2002)
        self.assertEqual(person.get_name(), 'Саша')

    def test_set_name(self):
        person = Person(name='Саша', year_of_birth=2002)
        person.set_name('Серега')
        self.assertEqual(person.name, 'Серега')

    def test_set_address(self):
        person = Person(name='Саша', year_of_birth=2002)
        person.set_address('Have')
        self.assertEqual(person.address, 'Have')

    def test_get_address(self):
        person = Person(name='Саша', year_of_birth=2002)
        self.assertEqual(person.address, '')

    def test_is_homeless_true(self):
        person = Person(name='Саша', year_of_birth=2002)
        self.assertTrue(person.is_homeless())

    def test_is_homeless_false(self):
        person = Person(name='Саша', year_of_birth=2002, address='Have')
        self.assertFalse(person.is_homeless())