from django.db import models
from userapp.models import Ombor
from asosiy.models import Client, Mahsulot

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.PositiveIntegerField()
    umumiy = models.PositiveIntegerField()
    tolandi = models.PositiveIntegerField()
    nasiya = models.PositiveIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

