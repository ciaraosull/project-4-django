from django.shortcuts import render


def profile(request):
    """Function to return the users profile template"""
    return render(request, 'profiles/profile-page.html')
