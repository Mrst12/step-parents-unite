""" Unit testing for Views """

from django.test import TestCase
from .models import Post


class TestIndexViews(TestCase):
    """ Unit test index page view """
    def test_get_index_page(self):
        """ function """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestPostListViews(TestCase):
    """ Unit test blog page view """
    def test_get_blog_page(self):
        """ function """
        response = self.client.get('/blog_page/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_page.html')

