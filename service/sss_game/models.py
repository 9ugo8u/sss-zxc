from django.db import models

class SssGame(models.Model):
    game = models.CharField(max_length=255)
    price = models.IntegerField()
    info = models.CharField(max_length=300)
