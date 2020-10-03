from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class board(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)
