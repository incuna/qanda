from django.core.urlresolvers import reverse
from django.test import TestCase


class TestAdmin(TestCase):
    def test_admin_url(self):
        """Is the admin available in the urls?"""
        url = reverse('admin:index')

        self.assertEqual(url, '/admin/')
