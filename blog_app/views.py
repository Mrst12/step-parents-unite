""" Views file for the blogs """

from django.shortcuts import render, get_object_or_404
from django.views import generic, View


def index(request):
    """ home page view """

    return render(request, 'index.html')
