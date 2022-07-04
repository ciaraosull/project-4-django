"""Url Patterns for Peer Code Review Platform"""
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentDeleteView,
    CommentUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-form'),
    path(
        'post/<slug:slug>/update/',
        PostUpdateView.as_view(),
        name='post-update'
        ),
    path(
        'post/<slug:slug>/delete/',
        PostDeleteView.as_view(),
        name='post-delete'
        ),
    path(
        'comments/<int:pk>/update/',
        CommentUpdateView.as_view(),
        name='comment-update'
        ),
    path(
        'comments/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment-delete'
        ),
]
