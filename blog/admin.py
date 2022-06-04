""" Imports for blog admin"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Class admin site post """
    list_display = ('project_title', 'slug', 'author', 'date_posted')
    search_fields = ['project-title', 'project_description']
    prepopulated_fields = {'slug': ('project_title', )}
    list_filter = ('date_posted', 'updated_on')
    summernote_fields = ('project_description')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'slug', 'post', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
