from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from api.views import UsersList 
from rest_framework import status
from django.core.urlresolvers import reverse


class UserReadTestCase(APITestCase):
    def test_can_read_user_list(self):
        response = self.client.get(reverse('api_show_user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)