from django.shortcuts import render
from django.http import HttpResponse
# import any models from classes created


def home(request):
    """ draft function view to test linking of url """
    return HttpResponse('<h1>Home Page</h1>')
