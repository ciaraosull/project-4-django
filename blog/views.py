from django.shortcuts import render
from django.views import generic
from .models import Post


# def home(request):
#     """ draft function view to test linking of url """
#     return render(request, 'index.html')

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-date_posted')
    template_name = 'index.html'
    paginate_by = 6
