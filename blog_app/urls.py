""" Blog post urls page"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog_page/', views.PostList.as_view(), name='blog_page'),
]
