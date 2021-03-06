from django.db import models
import random


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField()
    random_number = models.IntegerField(default=random.randint(1, 100))

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)