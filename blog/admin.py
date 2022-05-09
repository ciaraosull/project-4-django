""" Imports for blog admin"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Class admin site post """
    prepopulated_fields = {'slug': ('project_title', )}
    summernote_fields = ('project_description')
