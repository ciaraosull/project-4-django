"""Views to show the Profile Page"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import  UserUpdateForm, ProfileUpdateForm



@login_required
def profile(request):
    """Function to return the users profile template"""
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/profile-page.html', context)
