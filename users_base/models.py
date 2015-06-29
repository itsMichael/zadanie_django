from django.db import models
from django import forms


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField()
    random_number = models.IntegerField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.first_name+" "+self.last_name


class UserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name'})
        )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last name'})
        )
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'})
        )
