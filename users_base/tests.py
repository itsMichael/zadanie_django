from django.test import TestCase
from users_base.models import User
import unittest
from django.test import Client
from django.core.urlresolvers import reverse


class UserModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Janek", last_name="Kowalski", birthday="1900-11-22")
        User.objects.create(first_name="Janina", last_name="Kowalska", birthday="1990-10-20")

    def test_usermodel(self):
        one = User.objects.get(first_name="Janek")
        two = User.objects.get(first_name="Janina")
        self.assertEqual(one.last_name, "Kowalski")
        self.assertEqual(two.last_name, "Kowalska")        


class ViewIndexTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)


class ViewAddTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get(reverse('add'))

        self.assertEqual(response.status_code, 200)
