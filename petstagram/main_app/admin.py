from django.contrib import admin

from petstagram.main_app.models import Pet, Profile, PetPhoto


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', "date_of_birth"]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pets_type', "date_of_birth"]


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ['description', 'publication_date']


