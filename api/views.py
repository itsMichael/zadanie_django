from django.shortcuts import render
from api.serializers import UserListSerializer
from rest_framework import generics, filters
from users_base.models import User

class UsersFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'birthday', 'random_number']


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_class = UsersFilter
