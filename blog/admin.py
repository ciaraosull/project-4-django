""" Imports for blog admin"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Class admin site post """
    list_display = ('project_title', 'author', 'date_posted')
    prepopulated_fields = {"slug": ("project_title",)}
    search_fields = ['project-title', 'project_description']
    list_filter = ('date_posted', 'updated_on')
    summernote_fields = ('project_description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Class to display comments on admin site and approve"""
    list_display = ('name', 'your_comment', 'post', 'date_posted')
    list_filter = ('date_posted', 'name')
    search_fields = ('name', 'your_comment')
    #actions = ['approve_comments']

    #def approve_comments(self, request, queryset):
     #   queryset.update(approved=True)
