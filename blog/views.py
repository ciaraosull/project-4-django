from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    """ Class to show the posts in list view on home page """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate by = 6 goes here


class PostDetailView(DetailView):
    """ Class to show the individual posts in a detail view """
    model = Post
