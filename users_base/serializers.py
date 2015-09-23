from rest_framework import serializers
from users_base.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'birthday', 'random_number'
            )
