from django.db import models

class datas(models.Model):
    name = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=20, default="")   # phone numbers as text
    mail = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.name} ({self.contact})"
