from django.core.validators import ValidationError


def only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters')


def validate_max_size(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))
        return validate
