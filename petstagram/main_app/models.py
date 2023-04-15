from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=30, min_length= 2)
    last_name = models.CharField(max_length=30, min_length= 2)