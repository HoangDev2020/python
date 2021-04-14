from django.db import models
import datetime

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]
# Create your models here.

class Character(models.Model):
    name = models.CharField(null = True, blank = False, max_length = 50)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 20)
    age = models.IntegerField()
    img_Url = models.CharField(max_length = 400)
    bio = models.CharField(default = "", max_length = 50)
    created_at = models.DateField(default = datetime.date.today)