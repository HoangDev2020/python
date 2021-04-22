from django.db import models

# Create your models here.

import datetime
GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]

class User(models.Model):
    name = models.CharField(null = True, blank = False, max_length = 50)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 20)
    age = models.IntegerField()
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(default = datetime.datetime.now())