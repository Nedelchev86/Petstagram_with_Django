from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.main_app.validators import only_letters, validate_max_size


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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    FISH = "Fish"
    OTHER = "Other"
    PETS = [(x, x) for x in (CAT, DOG, BUNNY, FISH, OTHER)]

    name = models.CharField(max_length=30,)

    pets_type = models.CharField(
        max_length=max(len(x) for x, y in PETS),
        choices=PETS,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return f"{self.name} {self.pets_type}"

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(validate_max_size,)
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # Validate at least one Pet ( to do )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(default=0,)
