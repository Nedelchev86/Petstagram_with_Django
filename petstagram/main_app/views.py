from django.contrib import messages
from django.shortcuts import render, redirect

from petstagram.main_app.models import Profile, PetPhoto


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):

    context = {
        'hide_additional_nav_items': True
    }
    return render(request, "home_page.html", context)


def show_dashboard(request):
    profile = get_profile()

    if not profile:
        return redirect('401')

    pet_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, "dashboard.html", context)


def show_profile(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    total_images = len(pet_photos)
    total_like_count = sum(pp.likes for pp in pet_photos)

    context = {
        'profile': profile,
        'total_images': total_images,
        'total_images_likes': total_like_count,

    }
    return render(request, "profile_details.html", context)


def show_photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, "photo_details.html", context)


def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo details', pk)


