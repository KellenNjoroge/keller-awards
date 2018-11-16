from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from peewee import DoesNotExist
from .models import *
# from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import transaction


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    projects = Project.objects.filter(profile=current_user)

    return render(request, 'profile.html', {'profile': profile, 'images': projects})


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


def project(request, id):
    current_user = request.user
    project = Project.objects.get(id=id)
    averagevote = Vote.averagescore(id=id)
    if request.method == 'POST':
        voting_form = NewVote(request.POST)
        if voting_form.is_valid():
            vote = voting_form.save(commit=False)
            vote.voter = current_user
            vote.project = project
            vote.save()
        return redirect('index')
    else:
        voting_form = NewVote()

    return render(request, 'project.html', {'project': project,
                                                   'voting_form': voting_form})


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProject(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')

    else:
        form = NewProject()
    return render(request, 'new_post.html', {"form": form})


def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_query = request.GET.get("project")
        searched_projects = Project.objects.filter(projectname=search_query)
        print(search_query)
        message = f"{search_query}"
        print(searched_projects)

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
