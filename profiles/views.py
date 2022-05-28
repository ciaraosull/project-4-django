from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # decorator to ensure user is logged in to view this page
def profile(request):
    """Function to return the users profile template"""
    return render(request, 'profiles/profile-page.html')
