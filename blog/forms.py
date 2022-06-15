from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class CreatePostForm(forms.ModelForm):
    """ Create a Post Form """
    class Meta:
        """
        Get post model, choose fields to display and add summernote widget
        """
        model = Post
        fields = [
            'project_title',
            'project_description',
            'deployed_link',
            'code_repository',
            'other_relevant_information'
            ]

        widgets = {
            'project_description': SummernoteWidget(),
            }


class UpdatePostForm(forms.ModelForm):
    """ Update a Post Form """
    class Meta:
        """
        Get post model, choose fields to update and add summernote widget
        """
        model = Post
        fields = [
            'project_title',
            'project_description',
            'deployed_link',
            'code_repository',
            'other_relevant_information'
            ]

        widgets = {
            'project_description': SummernoteWidget(),
            }
