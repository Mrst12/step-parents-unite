""" Admin panel page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Use summernote for our content """
    summernote_fields = ('content')
