""" Unit testing for Views """

from django.test import TestCase
from .models import Post


class TestIndexViews(TestCase):
    """ Unit test index page view """
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')