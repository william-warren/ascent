from django.shortcuts import render, redirect
from showcase.forms import SignUp
from showcase.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def sign_up(request):
    if request.method == "GET":
        return render(request, "create-profile.html", {"form": SignUp()})
    elif request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            user = request.user
            headline = form.cleaned_data["headline"]
            bio = form.cleaned_data["bio"]
            codepen = form.cleaned_data["codepen"]
            github_repository = form.cleaned_data["github_repository"]
            profile = Profile.objects.create(
                user=user, headline=headline, bio=bio, codepen=codepen, github_repository=github_repository
            )
            return redirect("showcase:profile-list")
        else:
            return render(request, "create-profile.html", {"form": form})


def user_profiles(request):
    profiles = Profile.objects.all()
    return render(request, "user-profiles.html", {"profiles": profiles})


def profile_page(request, id):
    if request.method == "GET":
        profile = Profile.objects.get(id=id)
        return render(request, "profile-page.html", {"profile": profile})
