from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)
# from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-form'),
]
