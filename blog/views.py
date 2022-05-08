from django.shortcuts import render
# from django.views import generic
# import any models from classes created


def home(request):
    """ draft function view to test linking of url """
    return render(request, 'index.html')
