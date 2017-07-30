from django.db import models
from custom_user.models import AbstractEmailUser

class User(models.Model):
    account_id = models.AutoField(primary_key=True)

class Volunteer(AbstractEmailUser):
    first_name = models.CharField(max_length=20, blank = True)
    last_name = models.CharField(max_length=20, blank = True)
    phone = models.CharField(max_length=15, blank = True)
    hearts = models.SmallIntegerField(blank = True)
    badges = models.SmallIntegerField(blank = True)

