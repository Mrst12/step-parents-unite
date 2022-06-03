""" Unit Testing for forms """
from django.test import TestCase
from .forms import BlogForm, CommentForm


class TestBlogForm(TestCase):
    """ Unit test for blogs form """
    def test_post_title_is_required(self):
        """ title function """
        form = BlogForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    
    def test_post_content_is_required(self):
        """ content function"""
        form = BlogForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    
    def test_fields_are_explicit_in_form_metaclass(self):
        """ fields function """
        form = BlogForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'content', 'excerpt')
        )


