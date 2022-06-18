from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=30, blank=True)
    dokon = models.CharField(max_length=50, blank=True)
    manzil = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} ({self.dokon})"

