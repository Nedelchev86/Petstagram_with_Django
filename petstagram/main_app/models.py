from enum import unique
from random import choices

from django.db import models
from django.core.validators import MinLengthValidator

from petstagram import main_app
from petstagram.main_app import validators
from petstagram.main_app.validators import only_letters


# Create your models here.


class Profile(models.Model):
    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2), only_letters,
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2), only_letters,
        ]
    )
    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDER),
        choices=GENDER,
        null=True,
        blank=True,
    )


class Pet(models.Model):

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    FISH = "Fish"
    OTHER = "Other"
    PETS = [(x, x) for x in (CAT, DOG, BUNNY, FISH, OTHER)]

    name = models.CharField(max_length=30, unique=True,)
    pets_type = models.CharField(
        max_length=max(len(x) for x, y in PETS)
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )