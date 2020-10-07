from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class board(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)

class list(models.Model):
    parent_board = models.ForeignKey(board, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)

class card(models.Model):
    parent_list = models.ForeignKey(list, on_delete = models.CASCADE)
    label = models.CharField(max_length=50)
    due_date = models.DateTimeField(auto_now_add = False)
