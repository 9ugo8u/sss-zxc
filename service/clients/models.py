from django.contrib.auth.models import User
from django.db import models

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    wallet = models.IntegerField()