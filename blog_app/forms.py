""" Forms file for project"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Comment form"""
    class Meta:
        """ use comment model"""
        model = Comment
        fields = ('body',)
