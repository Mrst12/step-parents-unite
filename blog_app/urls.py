""" Blog post urls page"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog_page/', views.PostList.as_view(), name='blog_page'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_details'),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like'),
    path('profile', views.profile, name='profile'),
    path('publish', views.publish, name='publish'),
]
