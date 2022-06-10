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

from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostListView(ListView):
    """ Class to show the posts in list view on home page """
    model = Post  # model to use
    template_name = 'blog/index.html'  # set variable to html template name
    context_object_name = 'posts'  # name of variable to loop over in template
    ordering = ['-date_posted']  # order by most recent
    # paginate by = 6 goes here maybe


class PostDetailView(DetailView):
    """ Class to show the individual posts in a detail view """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Class to allow logged in users to create posts """
    model = Post
    fields = [
        'project_title',
        'project_description',
        'deployed_link',
        'code_repository',
        'other_relevant_information'
        ]
    widgets = {
        'project_description': SummernoteWidget(),
        }

    def form_valid(self, form):
        """Function to set signed in user as author of form to post"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # set author before running


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class to allow logged in users to update posts """
    model = Post
    fields = [
        'project_title',
        'project_description',
        'deployed_link',
        'code_repository',
        'other_relevant_information'
        ]
    widgets = {
        'project_description': SummernoteWidget(),
        }

    def form_valid(self, form):
        """Function to set signed in user as author of form to post"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # set author before running

    def test_func(self):
        "To ensure only the author of the post can update it"
        post = self.get_object()  # get the post to be update
        # ensure the logged in user is the author
        if self.request.user == post.author:
            return True  # if yes then update
        return False  # if not then 403 forbidden


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Class to allow the user of the post to delete it """
    model = Post
    success_url = '/'  # to redirect to home page after deleted

    def test_func(self):
        "To ensure only the author of the post can delete it"
        post = self.get_object()  # get the post to be update
        # ensure the logged in user is the author
        if self.request.user == post.author:
            return True  # if yes then delete
        return False  # if not then 403 forbidden
