""" Forms file for project"""

from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Comment form"""
    class Meta:
        """ use comment model"""
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    """ Form for user to publish own blog """
    class Meta:
        """ use post model"""
        model = Post
        fields = ('title', 'content', 'excerpt',)
