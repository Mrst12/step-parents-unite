""" Admin panel page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Use summernote for our content """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'approved')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    actions = ['approve_blogs']

    def approve_blogs(self, request, queryset):
        """ method for approving blogs"""
        queryset.update(status=1, approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Adding comment model to admin panel """

    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['author', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ Method for approving comments"""

        queryset.update(approved=True)
