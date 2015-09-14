from django.forms import ModelForm
from users_base.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday']