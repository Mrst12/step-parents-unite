""" Unit testing for Views """

from django.test import TestCase


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


class TestProfileViews(TestCase):
    """ unit test for profile page """
    def test_profile_page(self):
        """ function """
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestPublishBlogViews(TestCase):
    """ unit test for publish page """
    def test_can_publish_blog(self):
        """ function """
        response = self.client.get('/publish')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish.html')
