"""
Views to show the list of posts,
details of each post
create and delete posts
"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import CommentForm
from .forms import CreatePostForm, UpdatePostForm


class PostListView(ListView):
    """Class to show the posts in list view on home page """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate by = 6 goes here maybe


class PostDetailView(DetailView):
    """ Class to show the individual posts in a detail view """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Class to allow logged in users to create posts """
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        """Function to set signed in user as author of form to post"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class to allow logged in users to update posts """
    model = Post
    form_class = UpdatePostForm

    def form_valid(self, form):
        """Function to set signed in user as author of the form to post"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        To get the post to be updated
        and ensure only the author of the post can update it
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class to allow the user of the post to delete it 
    and then redirect back to home page
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
        To get the post to be updated
        and ensure only the author of the post can delete it
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCommentView(CreateView):
    """ Class to allow logged in users to comment """
    model = Post
    form_class = CommentForm
