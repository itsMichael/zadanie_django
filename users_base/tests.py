from django.test import TestCase
from users_base.models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Janek", last_name="Kowalski", birthday="1900-11-22")
        User.objects.create(first_name="Janina", last_name="Kowalska", birthday="1990-10-20")

    def test_usermodel(self):
        one = User.objects.get(first_name="Janek")
        two = User.objects.get(first_name="Janina")
        self.assertEqual(one.last_name, "Kowalski")
        self.assertEqual(two.last_name, "Kowalska")