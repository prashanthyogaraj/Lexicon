from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Login(models.Model):
    user = models.CharField(max_length=250)
    pswd = models.CharField(max_length=250)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
