from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
# from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-form'),
    path
    ('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path
    ('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
