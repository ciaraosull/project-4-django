from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     """ draft function view to test linking of url """
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/index.html', context)


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
