""" Unit Testing for forms """
from django.test import TestCase
from .forms import BlogForm, CommentForm


class TestBlogForm(TestCase):
    """ Unit test for blogs form """
    def test_post_title_is_required(self):
        """ function """
        form = BlogForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')