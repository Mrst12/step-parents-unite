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
    path('my_blogs', views.my_blogs, name='my_blogs'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('delete/<post_id>', views.delete_post, name='delete_blog'),
]
