from django.core.exceptions import ValidationError
from django.test import TestCase
from user_contacts.validators import validate_number, validate_string

class ValidatorTest(TestCase):
    def test_string_is_invalid_if_contains_numbers_or_special_characters(self):
        with self.assertRaises(ValidationError):
            validate_string('@test')
            validate_string('tester#')
    def test_number_is_invalid_if_contains_any_character_except_digits(self):
        with self.assertRaises(ValidationError):
            validate_number('123ABC')
            validate_number('75431#')



