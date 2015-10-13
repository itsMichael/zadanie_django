from django.test import TestCase
from users_base.models import User
from django.test import Client
from django.core.urlresolvers import reverse


class UserModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Janek", last_name="Kowalski", birthday="1900-11-22")
        User.objects.create(first_name="Janina", last_name="Kowalska", birthday="1990-10-20")

    def test_details(self):
        self.one = User.objects.get(first_name="Janek")
        self.two = User.objects.get(first_name="Janina")
        self.assertEqual(self.one.last_name, "Kowalski")
        self.assertEqual(self.two.last_name, "Kowalska")


class ViewIndexTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.myuser1 = User.objects.create(first_name="Stefan", last_name="Cebula", birthday="1994-10-20")
        self.myuser2 = User.objects.create(first_name="Slawomir", last_name="Cebula", birthday="1994-10-20")

    def test_details(self):
        self.response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue('object_list' in self.response.context)
        self.assertEqual([entry.pk for entry in self.response.context['object_list']], [self.myuser1.pk, self.myuser2.pk])
        self.assertEqual([entry.first_name for entry in self.response.context['object_list']], [self.myuser1.first_name, self.myuser2.first_name])


class ViewAddTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        self.post_response = self.client.post(reverse('add'), {'first_name': "jan", 'last_name': 'janowski', 'birthday': '1900-10-22'})
	self.assertEqual(self.post_response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)


class ViewEditTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.myuser = User.objects.create(first_name="Stefan", last_name="Cebula", birthday="1994-10-20")

    def test_details(self):
        self.post_response = self.client.post(reverse("edit", args=(self.myuser.id,)), {'first_name': "jan", 'last_name': 'janowski', 'birthday': '1900-10-22'})
	self.assertEqual(self.post_response.status_code, 302)
        self.assertEqual(User.objects.get(pk=self.myuser.pk).first_name, "jan")


class ViewDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.myuser = User.objects.create(first_name="Stefan", last_name="Cebula", birthday="1994-10-20")

    def test_my_get_request(self):
        self.response = self.client.get(reverse('remove', args=(self.myuser.id,)), follow=True)
	self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Are you sure you want to delete')

    def test_my_post_request(self):
        self.post_response = self.client.post(reverse('remove', args=(self.myuser.id,)), follow=True)
	self.assertEqual(self.post_response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)
