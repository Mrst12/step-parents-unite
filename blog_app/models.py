""" Database model for step-parents-unite blog app """

from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """ Post Model """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """ order by created on """
        ordering = ['-created_on']

    def __str__(self):
        """ return the title """
        return self.title

    def number_of_likes(self):
        """ number of likes """
        return self.likes.count()


class Comment(models.Model):
    """ Comments model """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ order by created on"""

        ordering = ['created_on']

    def __str__(self):
        """ return the content and author """

        return f"Comment {self.body} by {self.author}"
