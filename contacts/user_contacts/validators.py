import re
from django.core.exceptions import ValidationError

def validate_string(string):
	if re.search('^[A-Za-z]+$', string) is None:
		raise ValidationError('Invalid')

def validate_number(value):
	if re.search('^[0-9]+$', value) is None:
		raise ValidationError('Invalid')
