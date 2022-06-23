"""
Views to show the list of posts,
details of each post
create and delete posts
"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CreatePostForm, UpdatePostForm, CommentForm


class PostListView(ListView):
    """Class to show the posts in list view on home page """
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class PostDetailView(DetailView):
    """ Class to show the individual posts in a detail view """
    model = Post

    def post(self, request, slug):
        """
        To get the post by slug and display comment form
        if user is logged in.  If form is valid then,
        save the details of the comment form and include username
        """
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment_form.instance.post = post
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', post.slug)
        else:
            comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        """
        To display the comment form and
        paginate comments list if the user is logged in
        """
        context = super().get_context_data()
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        paginator = Paginator(comments, 6)
        page = self.request.GET.get('page')
        context['comments'] = paginator.get_page(page)
        context['page'] = page
        context['paginator'] = paginator
        context['comment_form'] = CommentForm()
        return context


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
