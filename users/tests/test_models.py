from django.test import TestCase
from incuna_test_utils.utils import field_names

from ..models import User


class TestUser(TestCase):
    def test_fields(self):
        expected = {
            'id',
            'email',
            'last_login',
            'name',
            'is_superuser',
            'password',

            'logentry',
            'groups',
            'user_permissions',
        }
        fields = field_names(User)

        self.assertEqual(fields, expected)
