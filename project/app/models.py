from django.db import models

class Count(models.Model):
    ammount = models.PositiveIntegerField(default=0)
