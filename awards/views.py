from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from peewee import DoesNotExist
from .models import *
# from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import transaction


def index(request):
    return render(request, 'index.html')


def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    # images = Image.objects.filter(profile = current_user)

    return render(request, 'profile.html', {'profile': profile})


@transaction.atomic
def update(request):
    # current_user = User.objects.get(pk=user_id)
    current_user = request.user
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES, instance=request.user)
        profile_form = EditProfile(request.POST, request.FILES, instance=current_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
        return redirect('profile')

    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=current_user.profile)
    return render(request, 'update.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })
