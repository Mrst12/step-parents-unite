""" Views file for the blogs """

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


def index(request):
    """ home page view """

    return render(request, 'index.html')


class PostList(generic.ListView):
    """ blog page view """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_page.html'
    paginate_by = 6
