from django.core.validators import ValidationError


def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters')
