"""
Views to show the list of posts,
details of each post
create and delete posts
"""
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
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


class PostCreateView(CreateView):
    """ Class to allow users to create posts """
    model = Post
    fields = [
        'project_title',
        'slug'
        'project_description',
        'deployed_link',
        'code_repository',
        'other_relevant_information'
        ]

    def form_valid(self, form):
        """Function to set signed in user as author of form to post"""
        form.instance.author = self.request.user
        return super().form_valid(form)  # set author before running
