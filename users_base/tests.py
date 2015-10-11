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
        User.objects.create(first_name="Stefan", last_name="Cebula", birthday="1994-10-20")
        User.objects.create(first_name="Slawomir", last_name="Cebula", birthday="1994-10-20")

    def test_details(self):
        self.response = self.client.get(reverse('home'))
        self.assertTrue('object_list' in self.response.context)
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual([entry.pk for entry in self.response.context['object_list']], [1, 2])
        self.assertEqual([entry.first_name for entry in self.response.context['object_list']], ["Stefan", "Slawomir"])


class ViewAddTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        self.client.post(reverse('add'), {'first_name': "jan", 'last_name': 'janowski', 'birthday': 1900-10-22})
        self.response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)
        print self.response
