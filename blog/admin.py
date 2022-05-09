""" Imports for blog admin"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Class admin site post """
    list_display = ('project_title', 'slug', 'author', 'date_posted')
    search_fields = ['project-title', 'project_description']
    prepopulated_fields = {'slug': ('project_title', )}
    list_filter = ('date_posted', 'updated_on')
    summernote_fields = ('project_description')
