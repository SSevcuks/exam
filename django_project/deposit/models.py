from django.db import models

class Deposit(models.Model):

    deposit = models.IntegerField(max_length=50)
    term = models.IntegerField(max_length=50)
    rate = models.FloatField(max_length=50)

