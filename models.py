from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=64)
    last_name = models.TextField(max_length=64)
    email = models.TextField(max_length=64)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(null=True)

    